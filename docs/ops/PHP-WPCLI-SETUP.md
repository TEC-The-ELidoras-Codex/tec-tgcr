# PHP + WP-CLI on Windows (optional)

Use this only if you need to test WordPress routes locally. For quick validation without installing PHP, use WordPress Playground instead (see bottom).

## Install PHP via winget

```powershell
# Install PHP
winget install --id PHP.PHP --source winget --silent

# Verify
php -v
```

## Install WP-CLI

```powershell
# Download wp-cli.phar to a known path (e.g., C:\Tools)
$dst = "C:\\Tools"; if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst | Out-Null }
Invoke-WebRequest https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -OutFile "$dst\wp-cli.phar"

# Create a shim script (wp.cmd) in the same folder for convenience
"@echo off`r`nphp \"%~dp0wp-cli.phar\" %*" | Out-File "$dst\wp.cmd" -Encoding ASCII

# Add to PATH for current session
$env:PATH = "$dst;$env:PATH"

# Verify
wp --info
```

## Using WP-CLI

From your WordPress install root (where wp-config.php lives):

```powershell
# List routes and filter for TEC
wp rest route list | Select-String tec

# Flush permalinks if needed
wp rewrite flush --hard
```

## WordPress Playground (no local PHP)

If you don’t want to install PHP locally:

- Launch WordPress Playground in your browser.
- Upload the TEC plugin ZIPs from `apps/wordpress/*`.
- Activate plugins and test routes under `/wp-json/...`.

This path is great for quick “does the route exist?” checks without local server setup.
