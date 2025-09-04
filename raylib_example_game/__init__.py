"""Raylib Example Game - A simple game using Raylib Python bindings."""

import asyncio
from importlib.metadata import version
__version__ = version("raylib-example-game")


def main():
    print(f"Raylib Example Game v{__version__}")
    from raylib_example_game.game import Game
    game = Game()
    asyncio.run(game.run())
