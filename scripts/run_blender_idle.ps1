param(
  [Parameter(Mandatory=$true)][string]$InputGlb,
  [Parameter(Mandatory=$false)][string]$OutputGlb = "ai-workflow/output/lumina_idle.glb",
  [Parameter(Mandatory=$false)][int]$Frames = 120,
  [Parameter(Mandatory=$false)][int]$Fps = 30,
  [Parameter(Mandatory=$false)][string]$Blender = "blender"
)

$script = "scripts/blender_headless_idle.py"

Write-Host "Running Blender headless idle on $InputGlb -> $OutputGlb"
& $Blender -b -P $script -- --input $InputGlb --output $OutputGlb --frames $Frames --fps $Fps