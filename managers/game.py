#!/usr/bin/env python3
import pygame
from actors.paddle import Paddle
from actors.ball import Ball
from actors.brick import Brick
""" Manages game initialization, screen, clock, main game loop """


class Game():
    """ Manages game initialization, screen, clock 

        Properties:
            screen: pygame screen
            clock: pyame clock
            isRunning: running state (if not true then stop game)
            deltaTime: time used for framerate independent physics calculations
    """
    bg_color = pygame.Color('black')

    def __init__(self, resolution: tuple, **kwargs) -> None:
        """ Initializes pygame with the screen resolution and arguments
            with whether it should be in testing mode or not
        """
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.scSize = resolution
        self.scHalf = (
            self.scSize[0] / 2, self.scSize[1] / 2)
        self.isRunning = True
        self.deltaTime = 0

        if 'testing' in kwargs:
            if kwargs['testing'] is True:
                self.testing = kwargs['testing']
                print('testing')
        else:
            self.testing = False

        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = Brick.makeBrickArray(self, 8)

    def play(self) -> None:
        """ Loops while self.isRunning is True """
        while (self.isRunning):
            # Get events
            for event in self.getEvents():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            self.screen.fill(self.bg_color)

            self.ball.updatePos(self.paddle)
            self.ball.draw()

            self.paddle.updatePos()
            self.paddle.draw()

            for brick in self.bricks:
                brick.draw()

            if self.testing is True:
                # print(self.ball.velocity)
                pygame.draw.circle(self.screen, 'red',
                                   (self.ball.rect.x, self.ball.rect.y), 3)
                pygame.draw.circle(self.screen, 'red',
                                   (self.paddle.rect.x, self.paddle.rect.y), 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.ball.rect.midbottom, 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.paddle.rect.midtop, 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.ball.rect.midright, 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.paddle.rect.midleft, 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.ball.rect.midleft, 3)
                pygame.draw.circle(self.screen, 'red',
                                   self.paddle.rect.midright, 3)
                # print(self.ball.rect.midbottom[1])
                self.drawTestPattern()

            self.deltaTime = self.deltaTick()
            self.nextFrame()

    def deltaTick(self) -> float:
        """ advances the frame and returns the delta time """
        return self.clock.tick(60) / 1000.0

    def drawTestPattern(self) -> None:
        """ Draws two white lines down the vertical and horizontal axis to 
            help test positioning
        """
        pygame.draw.line(self.screen, (255, 255, 255),
                         (0, self.scHalf[1]), (self.scSize[0], self.scHalf[1]))
        pygame.draw.line(self.screen, (255, 255, 255),
                         (self.scHalf[0], 0), (self.scHalf[0], self.scSize[1]))

    @staticmethod
    def nextFrame():
        pygame.display.flip()

    @staticmethod
    def getEvents():
        return pygame.event.get()

    @staticmethod
    def getKeys():
        return pygame.key.get_pressed()
