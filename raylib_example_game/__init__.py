"""Raylib Example Game - A simple game using Raylib Python bindings."""

__version__ = "0.1.0"


def main():
    from raylib_example_game.game import Game
    game = Game()
    game.run()