Param(
    [Parameter(Mandatory=$false)] [string]$BaseUrl = 'http://127.0.0.1:7860',
    [Parameter(Mandatory=$false)] [string]$ManifestPath = 'ai-workflow\\output\\consistency\\manifest.json',
    [Parameter(Mandatory=$false)] [string]$OutputDir = 'ai-workflow\\output\\renders\\consistency',
    [Parameter(Mandatory=$false)] [string]$Checkpoint = 'nova3DCGXL_ilV70.safetensors',
    [Parameter(Mandatory=$false)] [string]$LoraName = 'nova3dcgilv7.lrdE.safetensors',
    [Parameter(Mandatory=$false)] [double]$LoraWeight = 0.7,
    [switch]$DryRun
)

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { New-Item -ItemType Directory -Path $Path -Force | Out-Null }
}

function Read-PromptFile {
    param([string]$FilePath)
    $content = Get-Content -LiteralPath $FilePath -Raw
    $sections = @{}
    $current = ''
    foreach ($line in ($content -split "`r?`n")) {
        if ($line -match '^\s*POSITIVE PROMPT:') { $current = 'positive'; $sections[$current] = @(); continue }
        if ($line -match '^\s*NEGATIVE PROMPT:') { $current = 'negative'; $sections[$current] = @(); continue }
        if ($line -match '^\s*SETTINGS:') { $current = 'settings'; $sections[$current] = @(); continue }
        if ($current) { $sections[$current] += $line }
    }
    $pos = ($sections['positive'] -join "`n").Trim()
    $neg = ($sections['negative'] -join "`n").Trim()
    $sets = @{}
    foreach ($l in $sections['settings']) {
        if ($l -match '^\s*Steps:\s*(\d+)') { $sets['steps'] = [int]$Matches[1]; continue }
        if ($l -match '^\s*CFG Scale:\s*([0-9.]+)') { $sets['cfg_scale'] = [double]$Matches[1]; continue }
        if ($l -match '^\s*Size:\s*(\d+)x(\d+)') { $sets['width'] = [int]$Matches[1]; $sets['height'] = [int]$Matches[2]; continue }
        if ($l -match '^\s*Sampler:\s*(.+)$') { $sets['sampler'] = $Matches[1].Trim(); continue }
    }
    return [PSCustomObject]@{ positive=$pos; negative=$neg; settings=$sets }
}

function Set-Checkpoint {
    param([string]$ModelName)
    $body = @{ sd_model_checkpoint = $ModelName } | ConvertTo-Json
    Invoke-RestMethod -Uri "$BaseUrl/sdapi/v1/options" -Method POST -Body $body -ContentType 'application/json' | Out-Null
}

function Txt2Img {
    param(
        [string]$Prompt,
        [string]$NegativePrompt,
        [hashtable]$Settings
    )
    $payload = @{
        prompt = $Prompt
        negative_prompt = $NegativePrompt
        steps = $Settings.steps
        cfg_scale = $Settings.cfg_scale
        width = $Settings.width
        height = $Settings.height
        sampler_name = $Settings.sampler
        batch_size = 1
        n_iter = 1
        save_images = $true
        send_images = $true
    }
    $json = ($payload | ConvertTo-Json -Depth 5)
    if ($DryRun) { return @{ images=@(); info=$json } }
    return Invoke-RestMethod -Uri "$BaseUrl/sdapi/v1/txt2img" -Method POST -Body $json -ContentType 'application/json'
}

function Apply-Lora {
    param([string]$Prompt, [string]$LoraModel, [double]$Weight)
    if (-not $LoraModel) { return $Prompt }
    # Use file name without extension for LoRA tag to match WebUI naming
    $loraBase = [IO.Path]::GetFileNameWithoutExtension($LoraModel)
    # Insert LoRA trigger at the end of prompt
    $tag = "<lora:$($loraBase):$($Weight)>"
    if ($Prompt -match [regex]::Escape($tag)) { return $Prompt }
    if ($Prompt.Trim().EndsWith(',')) {
        return "$Prompt $tag"
    } else {
        return "$Prompt, $tag"
    }
}

Ensure-Directory -Path $OutputDir

if (-not (Test-Path -LiteralPath $ManifestPath)) {
    Write-Error "Manifest not found at $ManifestPath"; exit 1
}

$manifest = Get-Content -LiteralPath $ManifestPath -Raw | ConvertFrom-Json

# Ensure checkpoint
try {
    if (-not $DryRun -and $Checkpoint) { Set-Checkpoint -ModelName $Checkpoint }
} catch { Write-Warning "Failed to set checkpoint '$Checkpoint': $($_.Exception.Message)" }

$order = @('01_face_front','02_profile_left','04_upper_torso_front','05_wrists_closeup','06_back_view','07_full_body_turnaround','03_profile_right')
$items = @{}
foreach ($m in $manifest) { $items[$m.id] = $m }

foreach ($id in $order) {
    if (-not $items.ContainsKey($id)) { Write-Warning "Manifest missing id $id"; continue }
    $entry = $items[$id]
    $filePath = Join-Path (Get-Location) $entry.file
    if (-not (Test-Path -LiteralPath $filePath)) { Write-Warning "Prompt file missing: $filePath"; continue }
    Write-Host "Processing $id from $($entry.file)"
    $pf = Read-PromptFile -FilePath $filePath
    $pos = Apply-Lora -Prompt $pf.positive -LoraModel $LoraName -Weight $LoraWeight
    $res = Txt2Img -Prompt $pos -NegativePrompt $pf.negative -Settings $pf.settings
    if ($DryRun) {
        Write-Host "DRY RUN payload for ${id}:" ($res.info)
        continue
    }
    if ($res.images.Count -gt 0) {
        $bytes = [System.Convert]::FromBase64String($res.images[0])
        $outFile = Join-Path $OutputDir ("$id.png")
        [IO.File]::WriteAllBytes($outFile, $bytes)
        Write-Host "Saved $outFile"
    } else {
        Write-Warning "No image returned for $id"
    }
}

Write-Host "Done. Outputs (if not dry-run) in $OutputDir"
