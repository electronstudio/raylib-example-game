# Player

You can play this game on the web at http://electronstudio.github.io/raylib-example-game .  Works on mobile devices!

You can download binary releases for Windows, Macos and Linux from https://github.com/electronstudio/raylib-example-game/releases/latest

You can install this game from pypi:

    uv tool install raylib-example-game
    raylib-example-game


# Developer

## Python Implementation

This project defaults to **PyPy 3.11** for improved runtime performance.  To switch to CPython:

```bash
uv sync --python python3.13
```

## Raylib Backend

This project uses **`raylib_sdl`** instead of the standard `raylib` package for enhanced controller and gamepad compatibility.

If you prefer to use the standard Raylib backend, you can switch by updating the dependency:

```bash
# Remove raylib_sdl and add standard raylib
uv remove raylib_sdl
uv add raylib
```

**Backend Comparison:**
- **`raylib_sdl`**: Better controller/gamepad support, SDL backend
- **`raylib`**: Standard Raylib backend, potentially faster for basic graphics

The API is identical between both packages - no code changes are needed when switching.

## Setup

Install uv from https://docs.astral.sh/uv/getting-started/installation/

```bash
# Clone the repository
git clone https://github.com/yourusername/raylib-example-game.git
cd raylib-example-game

# Install in development mode
uv sync

# Run the game
uv run raylib-example-game
```



### Building the package

```bash
# Build wheel and source distribution
uv build
```

### Binary Compilation with Nuitka

```bash
uv run build-binary
```

**Creating Releases:**
```bash
# Tag and push to create a release with binaries
git tag v1.0.0
git push upstream v1.0.0
```

**Important:** The workflow requires `contents: write` permission to create GitHub releases. If release creation fails with a 403 error, check your repository's Actions permissions under Settings → Actions → General → Workflow permissions.



### Web Build with pygbag

Build for web deployment using pygbag:

```bash
# Build for web and start local server
uv run build-web

# Build for web only (no server)
uv run build-web --build
```

Github Actions automatically deploys the game to GitHub Pages on push to master.



