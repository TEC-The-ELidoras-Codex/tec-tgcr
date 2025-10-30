# Node.js for Local Development

This project contains components that may require Node.js for development or build steps.
This document explains recommended ways to install Node.js on Linux for development and how to use a container alternative.

## Recommended: nvm (per-user, no sudo)

nvm (Node Version Manager) lets you install and switch Node.js versions per-user without sudo. This is the safest and most flexible option for developers.

Install (example used when I ran these steps here):

```bash
# Install nvm (one-time)
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.6/install.sh | bash
# Then either open a new shell or source nvm in the current session:
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
# Install Node.js v24.11.0 (LTS)
nvm install 24.11.0
nvm alias default 24.11.0
# Verify
node -v   # => v24.11.0
npm -v    # => 11.6.1
```

Notes:
- No sudo required.
- You can install multiple Node versions and switch between them with `nvm use <version>`.
- This is the recommended approach for contributors working locally.

## Alternative: NodeSource apt repository (system-wide)

If you need a system-wide Node.js install (managed by apt), use the NodeSource repository. This requires sudo and is appropriate for servers or CI images.

```bash
# Example for Debian/Ubuntu (requires sudo)
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Container: Docker image (portable runtime)

If you prefer not to install Node on the host, use a Node Docker image (recommended for CI or containerized tasks):

```bash
# Pull the lightweight Alpine Node.js image
docker pull node:24-alpine
# Run an interactive shell
docker run -it --rm --entrypoint sh node:24-alpine
# Inside the container, verify version
node -v
npm -v
```

I pulled `node:24-alpine` in the dev environment for you. Use Docker when you want reproducible, containerized runs.

## Notes for this repository

- I installed Node.js v24.11.0 via `nvm` for the current user and pulled the `node:24-alpine` Docker image.
- If you want, I can add NPM/Yarn build steps or a small `Makefile` target to run common tasks, e.g. `make js-build` or `make js-shell` that uses the Docker image.
