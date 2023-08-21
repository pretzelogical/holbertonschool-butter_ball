#!/usr/bin/env python3
import pygame
from sys import argv
from actors.paddle import Paddle
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

    def play(self) -> None:
        """ Loops while self.isRunning is True """
        while (self.isRunning):
            # Get events
            for event in self.getEvents():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            self.screen.fill(self.bg_color)
            if self.testing is True:
                self.drawTestPattern()

            self.paddle.updatePos()
            self.paddle.draw()

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
