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
        self.font = pygame.font.Font(None, 36)
        self.scHalf = (
            self.scSize[0] / 2, self.scSize[1] / 2)
        self.isRunning = True
        self.deltaTime = 0
        self.lives = 3
        self.rows = 3
        pygame.display.set_caption('Butter ball')

        self.background = pygame.image.load('img/dinerbg.jpg')
        #self.background = pygame.image.load('img/pancakebg2.0.jpg')
        self.background = pygame.transform.scale(self.background, resolution)

        if 'testing' in kwargs:
            if kwargs['testing'] is True:
                self.testing = kwargs['testing']
                print('testing')
        else:
            self.testing = False

        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = Brick.makeBrickArray(self, self.rows)

    def play(self) -> None:
        """ Loops while self.isRunning is True """
        while (self.isRunning):
            # Get events
            for event in self.getEvents():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            self.screen.fill(self.bg_color)
            self.screen.blit(self.background, (0, 0))

            self.ball.updatePos(self.paddle)
            self.ball.draw()

            self.paddle.updatePos()
            self.paddle.draw()

            for brick in self.bricks:
                brick.draw()

            self.screen.blit(self.font.render(
                str(self.lives), True, 'white'), (self.scHalf[0], self.scHalf[1] / 6))

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
                keys = pygame.key.get_pressed()
                if keys[pygame.K_n]:
                    self.bricks = []
                self.drawTestPattern()

            self.deltaTime = self.deltaTick()
            self.nextFrame()

            if len(self.bricks) == 0:
                self.roundNext()

            if self.lives == 'Game over!':
                pygame.time.wait(3000)
                self.isRunning = False

    def deltaTick(self) -> float:
        """ advances the frame and returns the delta time """
        return self.clock.tick(60) / 1000.0

    def roundOver(self):
        """ Called whenever the ball goes out of play """
        pygame.time.wait(1000)
        self.ball.velocity = self.ball.initVel
        self.ball.isHeld = True
        self.lives -= 1
        if self.lives == 0:
            self.lives = 'Game over!'

    def roundNext(self):
        """ Starts a new round """
        pygame.time.wait(3000)
        self.rows += 1
        self.lives += 1
        self.bricks = Brick.makeBrickArray(self, self.rows)
        self.ball.velocity.x = abs(self.ball.velocity.x) + 50
        self.ball.velocity.y = abs(self.ball.velocity.y) + 50
        self.paddle.moveSpeed += 50
        self.ball.isHeld = True

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
