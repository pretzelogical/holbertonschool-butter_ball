#!/usr/bin/env python3
""" imports and initializes the game"""
from managers.game import Game
from sys import argv
SC_RES = (1000, 750)

game_kwargs = {}
if 'test' in argv:
    game_kwargs['testing'] = True


game = Game(SC_RES, **game_kwargs)

game.play()
