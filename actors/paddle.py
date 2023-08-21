#!/usr/bin/env python3
import pygame
""" Defines a movable paddle """


class Paddle():
    """ Movable paddle

        Properties:
            __game: the game object that manages the paddle
            width: width of the collision box
            height: height of the collision box
            initPos: position to start paddle in new round
            moveSpeed: multiplied against deltatime to get movement
            rect: rectanglular representation of the paddle
    """
    color = pygame.Color('white')

    def __init__(self, game) -> None:
        self.__game = game
        self.width = game.scSize[0] / 8
        self.height = game.scSize[1] / 16
        self.initPos = pygame.Vector2(
            game.scHalf[0] - (self.width / 2), game.scHalf[1] + (game.scHalf[1] * 0.85))
        self.moveSpeed = 350
        self.rect = pygame.Rect(self.initPos.x, self.initPos.y,
                                self.width, self.height)

    def updatePos(self):
        keys = self.__game.getKeys()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.moveSpeed * self.__game.deltaTime
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.moveSpeed * self.__game.deltaTime
        self.rect.x = max(
            0, min(self.rect.x, self.__game.scSize[0] - self.width))

    def draw(self):
        pygame.draw.rect(self.__game.screen, self.color, self.rect)
        