# Raylib Example Game

A simple game example using Raylib Python bindings, demonstrating modern Python packaging with `uv`.

## Features

- Simple Raylib game window with text rendering
- Modern Python packaging with `pyproject.toml`
- Clean modular architecture
- Console script entry point

## Requirements

- Python 3.11 or higher
- `uv` package manager (recommended) or `pip`
- **Default**: PyPy 3.11 (for better performance)

## Python Implementation

This project defaults to **PyPy 3.11** for improved runtime performance, especially beneficial for game loops and real-time graphics. The game will display which Python implementation is being used when it starts.

### Switching Python Implementations

**Use CPython instead of PyPy:**
```bash
# For development
uv sync --python python3.13
uv run main.py

# For one-time execution
uv run --python python3.13 main.py
```

**Use specific PyPy versions:**
```bash
# PyPy 3.10
uv run --python pypy3.10 main.py

# Latest PyPy
uv run --python pypy main.py
```

**Performance Notes:**
- **PyPy**: Faster execution for game logic, longer startup time
- **CPython**: Faster startup, may be slower for intensive computations

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/raylib-example-game.git
cd raylib-example-game

# Install in development mode
uv sync

# Run the game
uv run raylib-example-game
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/raylib-example-game.git
cd raylib-example-game

# Install in development mode
pip install -e .

# Run the game
raylib-example-game
```

### Install from PyPI (when published)

```bash
# Using uv
uv add raylib-example-game

# Using pip
pip install raylib-example-game
```

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/raylib-example-game.git
cd raylib-example-game

# Install with uv
uv sync

# Run in development mode
uv run main.py
```

### Building the package

```bash
# Build wheel and source distribution
uv build
```

## Usage

Once installed, you can run the game using:

```bash
raylib-example-game
```

Or run the module directly:

```bash
python -m raylib_example_game
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.