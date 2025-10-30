<#
.SYNOPSIS
Moves a local repository out of OneDrive to a new local path while preserving the .git directory.

.DESCRIPTION
This script copies the current repository directory to a destination path you provide.
It verifies the copy, ensures the destination contains the .git directory, runs a quick git status,
and runs the project's pytest to validate the move.

USAGE
.\move_repo_from_onedrive.ps1 -Destination 'C:\Projects\tec-tgcr'

#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$Destination
)

function Abort($msg){ Write-Error $msg; exit 1 }

$source = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent | Split-Path -Parent
Write-Host "Detected source repo root: $source"

if ($Destination -eq $source) { Abort "Destination equals source. Choose a different destination." }

if (Test-Path $Destination) {
    Write-Host "Destination exists. Will attempt to copy into existing path: $Destination"
} else {
    Write-Host "Creating destination path: $Destination"
    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
}

Write-Host "Copying files (this may take a while)..."
try {
    # Use robocopy for robust copy on Windows
    $robocopyExe = (Get-Command robocopy -ErrorAction SilentlyContinue)
    if ($null -ne $robocopyExe) {
        $rcArgs = @($source, $Destination, "/MIR", "/COPYALL", "/R:3", "/W:5")
        Write-Host "Running: robocopy $($rcArgs -join ' ')"
        & robocopy @rcArgs | Write-Host
    } else {
        Copy-Item -Path "$source\*" -Destination $Destination -Recurse -Force -ErrorAction Stop
    }
} catch {
    Abort "Copy failed: $_"
}

if (-not (Test-Path (Join-Path $Destination '.git'))) {
    Write-Warning ".git not found in destination. The repository metadata may not have been copied correctly."
    Write-Host "Attempting to copy hidden files explicitly..."
    Get-ChildItem -Path $source -Force -Include '.git' -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
        $target = $_.FullName.Replace($source, $Destination)
        if ($_.PSIsContainer) { New-Item -ItemType Directory -Path $target -Force | Out-Null }
        Copy-Item -Path $_.FullName -Destination $target -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "Verifying destination..."
Set-Location -Path $Destination

if (-not (Test-Path '.git')) {
    Abort "Destination does not contain a .git directory. Manual intervention required."
}

Write-Host "Running git status in destination..."
try {
    git status --porcelain
} catch {
    Write-Warning "git command failed; ensure git is installed and on PATH in this session."
}

Write-Host "Running pytest in destination to validate..."
try {
    if (Test-Path '.venv\Scripts\python.exe') {
        .\.venv\Scripts\python.exe -m pytest -q
    } else {
        python -m pytest -q
    }
} catch {
    Write-Warning "pytest returned non-zero exit — review test output in the destination environment."
}

Write-Host "Move complete. Next steps:"
Write-Host " - Open the destination folder in VS Code (File → Open Folder)."
Write-Host " - If using OneDrive syncing, consider pausing sync for the destination folder."
Write-Host " - Update any local tooling paths (scripts, shortcuts) that pointed to the old OneDrive location."
