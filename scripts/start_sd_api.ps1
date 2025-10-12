Param(
    [Parameter(Mandatory=$false)] [string]$WebUIPath,
    [Parameter(Mandatory=$false)] [int]$Port = 7860,
    [switch]$Medvram,
    [switch]$Xformers,
    [switch]$NoHalfVae,
    [switch]$Listen,
    [switch]$SkipModelCheck
)

function Find-WebUIPath {
    Param([string]$Hint)
    if ($Hint -and (Test-Path -LiteralPath (Join-Path $Hint 'webui-user.bat'))) {
        return (Resolve-Path -LiteralPath $Hint).Path
    }
    if ($env:SD_WEBUI_PATH -and (Test-Path -LiteralPath (Join-Path $env:SD_WEBUI_PATH 'webui-user.bat'))) {
        return (Resolve-Path -LiteralPath $env:SD_WEBUI_PATH).Path
    }
    $candidates = @(
        'C:\stable-diffusion-webui',
        'C:\AI\stable-diffusion-webui',
        "$env:USERPROFILE\stable-diffusion-webui",
        "$env:USERPROFILE\Desktop\stable-diffusion-webui"
    )
    foreach ($c in $candidates) {
        if (Test-Path -LiteralPath (Join-Path $c 'webui-user.bat')) { return (Resolve-Path -LiteralPath $c).Path }
    }
    return $null
}

function Wait-PortOpen {
    Param([string]$Host='127.0.0.1', [int]$Port=7860, [int]$TimeoutSec=180)
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    while ($sw.Elapsed.TotalSeconds -lt $TimeoutSec) {
        try {
            $tcp = New-Object System.Net.Sockets.TcpClient
            $iar = $tcp.BeginConnect($Host, $Port, $null, $null)
            $connected = $iar.AsyncWaitHandle.WaitOne(1000, $false)
            if ($connected -and $tcp.Connected) {
                $tcp.EndConnect($iar)
                $tcp.Close()
                return $true
            }
            $tcp.Close()
        } catch { }
        Start-Sleep -Seconds 1
    }
    return $false
}

$resolvedPath = Find-WebUIPath -Hint $WebUIPath
if (-not $resolvedPath) {
    Write-Error "Stable Diffusion WebUI not found. Pass -WebUIPath or set SD_WEBUI_PATH env var to the folder that contains webui-user.bat."
    exit 1
}

$argsList = @('--api', "--port $Port")
if ($Medvram) { $argsList += '--medvram' }
if ($Xformers) { $argsList += '--xformers' }
if ($NoHalfVae) { $argsList += '--no-half-vae' }
if ($Listen) { $argsList += '--listen' }

$env:COMMANDLINE_ARGS = ($argsList -join ' ')
Write-Host "Launching WebUI at $resolvedPath with args: $env:COMMANDLINE_ARGS"

$bat = Join-Path $resolvedPath 'webui-user.bat'
if (-not (Test-Path -LiteralPath $bat)) {
    Write-Error "webui-user.bat not found at $bat"
    exit 1
}

Start-Process -FilePath $bat -WorkingDirectory $resolvedPath -WindowStyle Normal

Write-Host "Waiting for API to be available on port $Port..."
if (Wait-PortOpen -Host '127.0.0.1' -Port $Port -TimeoutSec 300) {
    Write-Host "API is up at http://127.0.0.1:$Port"
} else {
    Write-Error "Timed out waiting for API on http://127.0.0.1:$Port"
    exit 2
}

if (-not $SkipModelCheck) {
    try {
        $baseUrl = "http://127.0.0.1:$Port"
        $options = Invoke-RestMethod -Uri "$baseUrl/sdapi/v1/options" -Method GET -TimeoutSec 10
        Write-Host "Current model checkpoint: $($options.sd_model_checkpoint)"
    } catch {
        Write-Warning "API reachable but failed to query options: $($_.Exception.Message)"
    }
}
