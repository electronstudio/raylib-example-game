# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python game project using Raylib Python bindings (`raylib-sdl`) with modern packaging via `uv`. The project defaults to **PyPy 3.11** for improved runtime performance in game loops.

## Essential Commands

### Development Setup
```bash
# Install dependencies and create virtual environment
uv sync

# Run the game in development mode
uv run main.py

# Or run via console script entry point
uv run raylib-example-game
```

### Building and Distribution
```bash
# Build Python wheel and source distribution
uv build

# Build standalone binary with Nuitka (automatically uses CPython 3.13)
uv run build-binary

# Manual Nuitka build with specific Python version
uv run --python python3.13 python -m nuitka --onefile main.py
```

### Python Version Management
```bash
# Switch to CPython for development
uv sync --python python3.13
uv run --python python3.13 main.py

# Use specific PyPy versions
uv run --python pypy3.10 main.py
```

## Architecture

### Project Structure
- `main.py` - Entry point that imports and runs the Game class
- `raylib_example_game/` - Main package directory
  - `__init__.py` - Package initialization with main() function
  - `game.py` - Core Game class with window management and game loop
- `scripts/` - Utility scripts
  - `build.py` - Nuitka build automation script

### Core Architecture
- **Game Class** (`raylib_example_game/game.py`): Main game controller with configurable window dimensions, title, and FPS management
- **Entry Points**: Multiple ways to run the game:
  - Console script: `raylib-example-game` 
  - Module execution: `python -m raylib_example_game`
  - Direct execution: `python main.py`

### Dependencies
- **raylib-sdl**: Enhanced Raylib with SDL backend for better controller support
- **nuitka**: Optional binary compilation (dev dependency)
- Uses PyPy 3.11 by default (specified in `.python-version`)

## Key Technical Details

### Python Implementation Strategy
- **Default**: PyPy 3.11 for runtime performance
- **Binary builds**: Automatically switches to CPython 3.13 (Nuitka requirement)
- **Development**: Can use any Python 3.11+

### Raylib Backend
Uses `raylib-sdl` instead of standard `raylib` for enhanced controller/gamepad compatibility. API is identical between backends.

### Build System
- **Package management**: `uv` (modern pip replacement)
- **Build backend**: Hatchling
- **Binary compilation**: Nuitka with optimizations enabled