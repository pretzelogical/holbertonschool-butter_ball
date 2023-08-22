#!/usr/bin/env python3
import pygame
""" Defines a brick that breaks upon colliding with the ball """


class Brick:
    """ Brick that breaks upon colliding with the ball """
    color = pygame.Color('tan')

    def __init__(self, game, pos: tuple) -> None:
        """ Creates brick and assigns private game variable """
        self.__game = game
        self.width = 100
        self.height = 110
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)

        self.image = pygame.image.load('img/pancakebrick.png')
        self.image = pygame.transform.scale(
            self.image, (int(self.width), int(self.height)))

    def draw(self):
        """ Draws the brick """
        # pygame.draw.rect(self.__game.screen, self.color, self.rect)
        self.__game.screen.blit(self.image, self.rect.topleft)

    @staticmethod
    def makeBrickArray(game, rows):
        """ Creates an array of bricks to be placed onscreen
            rows: amount of rows
        """
        rows *= 8
        bricks = []
        gap = game.scHalf[0] / 6
        gapSpace = gap
        leftMost = (game.scHalf[0] / 3) + gap * 0.08
        vertical = game.scHalf[1] / 4
        for i in range(1, rows + 1):
            if (i - 1) % 8 == 0:
                gapSpace = gap
                vertical += game.scHalf[1] / 8
            if i == 1 or (i - 1) % 8 == 0:
                bricks.append(
                    Brick(game, (leftMost, vertical)))
            else:
                bricks.append(
                    Brick(game, (leftMost + gapSpace, vertical)))
                gapSpace += gap
        return bricks
