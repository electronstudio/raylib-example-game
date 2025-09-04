"""Raylib Example Game - A simple game using Raylib Python bindings."""

import asyncio

def main():
    from raylib_example_game.game import Game
    game = Game()
    asyncio.run(game.run())
