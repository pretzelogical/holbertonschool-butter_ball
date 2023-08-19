#!/usr/bin/env python3
""" Handles drawing and physics for ball """
import pygame


class Ball:
    """ Handles drawing and physics for ball"""

    def __init__(self, game):
        self.__game = game
        self.size = game.scSize[0] / 8
        self.initPos = pygame.Vector2(
            game.scHalf[0] - (self.size / 2), game.scHalf[1] - (self.size / 2))
        self.rect = pygame.Rect(
            self.initPos.x, self.initPos.y, self.size, self.size)
