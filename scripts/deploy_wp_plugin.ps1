# Deploy the packaged WordPress.com plugin via SFTP using a key file path
# Usage:
#   pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/deploy_wp_plugin.ps1 [-ZipPath <path-to-zip>]
#
# Reads the following environment variables (prefer .env.local loaded into session):
#   WPCOM_SSH_HOST                  (e.g., sftp.wp.com)
#   WPCOM_SSH_PORT                  (default: 22)
#   WPCOM_SSH_USER                  (e.g., yoursite.wordpress.com)
#   WPCOM_SSH_TARGET                (e.g., /htdocs/wp-content/plugins/tec-tgcr)
#   WPCOM_SSH_PRIVATE_KEY_PATH      (absolute path to private key file)
#
# This script intentionally uses a key PATH, not inline key content.

param(
    [string]$ZipPath = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$workspace = (Resolve-Path "$PSScriptRoot/..\").Path

# Resolve ZIP path: if not provided, pack first and use latest artifact
if (-not $ZipPath) {
    & pwsh -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'pack_wp_plugin.ps1')
    $outDir = Join-Path $workspace 'exports/wp-plugin'
    if (-not (Test-Path $outDir)) { throw "Output directory not found: $outDir" }
    $latest = Get-ChildItem -LiteralPath $outDir -Filter 'tec-tgcr-*.zip' | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if (-not $latest) { throw "No packaged ZIP found in $outDir" }
    $ZipPath = $latest.FullName
}

if (-not (Test-Path $ZipPath)) { throw "ZIP not found: $ZipPath" }

$sshHost = $env:WPCOM_SSH_HOST
$sshPort = if ($env:WPCOM_SSH_PORT) { [int]$env:WPCOM_SSH_PORT } else { 22 }
$sshUser = $env:WPCOM_SSH_USER
$sshTarget = $env:WPCOM_SSH_TARGET
$sshKeyPath = $env:WPCOM_SSH_PRIVATE_KEY_PATH

if (-not $sshHost)   { throw "WPCOM_SSH_HOST not set" }
if (-not $sshUser)   { throw "WPCOM_SSH_USER not set" }
if (-not $sshTarget) { throw "WPCOM_SSH_TARGET not set" }
if (-not $sshKeyPath) { throw "WPCOM_SSH_PRIVATE_KEY_PATH not set" }
if (-not (Test-Path $sshKeyPath)) { throw "Private key file not found: $sshKeyPath" }

Write-Host ("[deploy] Host   : {0}:{1}" -f $sshHost, $sshPort)
Write-Host "[deploy] User   : $sshUser"
Write-Host "[deploy] Target : $sshTarget"
Write-Host "[deploy] ZIP    : $ZipPath"
Write-Host "[deploy] Key    : $sshKeyPath"

# Create a temporary SFTP batch file
$tmp = New-TemporaryFile
try {
    @(
        "cd $sshTarget",
        "put `"$ZipPath`""
    ) | Set-Content -LiteralPath $tmp -Encoding ASCII

    # Use Windows OpenSSH sftp client with batch mode
    # -P for port, -i for identity file
    $sftpArgs = @('-b', $tmp, '-P', $sshPort, '-i', $sshKeyPath, ("{0}@{1}" -f $sshUser, $sshHost))
    Write-Host "[deploy] Running: sftp $($sftpArgs -join ' ')"
    $proc = Start-Process -FilePath 'sftp' -ArgumentList $sftpArgs -NoNewWindow -Wait -PassThru
    if ($proc.ExitCode -ne 0) { throw "sftp exited with code $($proc.ExitCode)" }

    Write-Host "[deploy] Upload complete."
}
finally {
    if (Test-Path $tmp) { Remove-Item -LiteralPath $tmp -Force }
}
