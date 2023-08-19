#!/usr/bin/env python3
""" Handles drawing and physics for ball """
import pygame


class Ball:
    """ Handles drawing and physics for ball"""
    color = pygame.Color('white')

    def __init__(self, game):
        self.__game = game
        self.size = game.scSize[0] / 24
        self.initPos = pygame.Vector2(
            game.scHalf[0] - (self.size / 2), game.scHalf[1] - (self.size / 2))
        self.rect = pygame.Rect(
            self.initPos.x, self.initPos.y, self.size, self.size)
        self.velocity = pygame.Vector2(200, 200)

    def updatePos(self):
        """ Updates ball position  with velocity """
        self.rect.x += self.velocity.x * self.__game.deltaTime
        self.rect.y += self.velocity.y * self.__game.deltaTime
        print(self.velocity.x)

        if self.rect.x < 0 or self.rect.x > self.__game.scSize[0] - self.size:
            print('ping!')
            self.velocity.x *= -1
        if self.rect.y < 0 or self.rect.y > self.__game.scSize[1] - self.size:
            print('ping!')
            self.velocity.y *= -1

    def draw(self):
        pygame.draw.rect(self.__game.screen, self.color, self.rect)
