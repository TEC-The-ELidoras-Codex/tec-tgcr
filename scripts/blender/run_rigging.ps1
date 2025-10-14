# Runs Blender in background to auto-rig a Lumina GLB using Rigify

param(
    [string]$BlenderExe = "C:\\Program Files\\Blender Foundation\\Blender 4.1\\blender.exe",
    [string]$GlbPath = "C:\\Users\\Ghedd\\OneDrive - TEC - The Elidoras Codex\\Projects\\TEC\\tec-tgcr\\data\\digital_assets\\Copilot3D-caacd028-fd38-4a13-8092-a63f27c8f45c.glb",
    [string]$OutputPrefix = "C:\\Users\\Ghedd\\OneDrive - TEC - The Elidoras Codex\\Projects\\TEC\\tec-tgcr\\data\\digital_assets\\lumina_rigged",
    [float]$Scale = 1.0,
    [switch]$NoJoin
)

$scriptPath = "${PSScriptRoot}\\rig_lumina.py"

if (-not (Test-Path $BlenderExe)) {
    Write-Error "Blender executable not found: $BlenderExe"
    exit 1
}
if (-not (Test-Path $GlbPath)) {
    Write-Error "GLB file not found: $GlbPath"
    exit 1
}
if (-not (Test-Path $scriptPath)) {
    Write-Error "Rig script not found: $scriptPath"
    exit 1
}

$argsList = @(
    "-b",
    "-P", $scriptPath,
    "--",
    "--glb", $GlbPath,
    "--output", $OutputPrefix,
    "--scale", $Scale
)
if ($NoJoin) { $argsList += "--no_join" }

& $BlenderExe @argsList
