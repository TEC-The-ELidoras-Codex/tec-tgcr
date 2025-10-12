param(
  [Parameter(Mandatory=$true, Position=0)]
  [string] $Url
)

# PowerShell wrapper that calls the Python sanitizer if available.
# Falls back to simple rewrite without network calls.

function Invoke-PythonSanitizer {
  try {
    $cmd = "python"
    $py = "$PSScriptRoot\sanitize_spotify_url.py"
    if (Test-Path $py) {
      $result = & $cmd $py $Url 2>$null
      if ($LASTEXITCODE -eq 0 -and $result) {
        $result
        return $true
      }
    }
  } catch {}
  return $false
}

if (Invoke-PythonSanitizer) { exit 0 }

# Simple fallback: try to match open.spotify.com/<type>/<id>
$regex = [regex] '^(?:https?://)?(?:open\.)?spotify\.com/(?<type>track|album|playlist|artist|episode|show)/(?<id>[A-Za-z0-9]+)'
$m = $regex.Match($Url)
if (-not $m.Success) {
  Write-Error "Unsupported Spotify URL path. Expected /{type}/{id}."
  exit 1
}

$kind = $m.Groups['type'].Value.ToLower()
$sid = $m.Groups['id'].Value
$canonical = "https://open.spotify.com/$kind/$sid"
$embed = "https://open.spotify.com/embed/$kind/$sid"

[PSCustomObject]@{
  kind = $kind
  id = $sid
  canonical_url = $canonical
  embed_url = $embed
} | ConvertTo-Json -Depth 3
