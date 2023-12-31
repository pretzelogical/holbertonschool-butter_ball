#!/usr/bin/env python3
""" Handles drawing and physics for ball """
import pygame


class Ball:
    """ Handles drawing and physics for ball"""
    color = pygame.Color('white')

    def __init__(self, game):
        """ Ball that moves across the screen

            Properties:
                __game: the game object that manages the ball
                size: the size of the ball
                initPos: initial position of the ball
                rect: rectangular representation of the ball
                initVel: inital velocity of the ball
                velocity: applied to x and y of the rect every frame
                isHeld: if the ball is being held by the paddle
        """
        self.__game = game
        self.size = game.scSize[0] / 24
        self.initPos = pygame.Vector2(
            game.scHalf[0] - (self.size / 2), game.scHalf[1] - (self.size / 2))
        self.rect = pygame.Rect(
            self.initPos.x, self.initPos.y, self.size, self.size)
        self.initVel = pygame.Vector2(200, 200)
        self.velocity = self.initVel
        self.isHeld = True

        self.image = pygame.image.load('img/butter5.0.png')
        self.image = pygame.transform.scale(
            self.image, (int(self.size), int(self.size)))

    def updatePos(self, paddle):
        """ Updates ball position with velocity and collision unless it is held
        then position it on the top of the paddle to be launched"""
        if self.isHeld:
            self.rect.y = paddle.rect.y - self.size - (self.size / 4)
            self.rect.x = paddle.rect.x + self.size
            if self.__game.getKeys()[pygame.K_SPACE]:
                self.isHeld = False
            return
        self.rect.x += self.velocity.x * self.__game.deltaTime
        self.rect.y += self.velocity.y * self.__game.deltaTime

        if self.rect.colliderect(paddle.rect):
            self.paddleCollision(paddle)

        self.screenCollision()

        brickCollide = pygame.Rect.collidelist(self.rect, self.__game.bricks)
        if brickCollide != -1:
            self.brickCollision(brickCollide)

    def screenCollision(self):
        """ Checks all sides of the screen for collision and repositions
        ball if it is outside of the horizontal screen boundry.
        """

        if self.rect.x < 0 or self.rect.x > self.__game.scSize[0] - self.size:
            self.velocity.x *= -1
        if self.rect.y < 0:
            self.velocity.y *= -1

        if self.rect.midbottom[1] > self.__game.scSize[1]:
            if self.__game.testing:
                print('ballout')
            self.__game.roundOver()
        if self.rect.x < -4:
            if self.__game.testing:
                print('left x over')
            self.rect.x = 0
        if self.rect.x > 4 + (self.__game.scSize[0] - self.size):
            if self.__game.testing:
                print('right x over')
        if self.rect.y < -4:
            if self.__game.testing:
                print('top over')
            self.rect.y = 0

    def brickCollision(self, brickId):
        """ Bounces off a brick and removes that brick """
        brickId = brickId
        brick = self.__game.bricks[brickId]
        detected = False
        if self.__game.testing:
            print(f"ball collided with brick # {brickId}")
        # Ball hits brick on top
        if abs(self.rect.midbottom[1] - brick.rect.midtop[1]) < 16:
            if self.__game.testing:
                print('bricktophit')
            self.velocity.y *= -1
            detected = True
        # Ball hits brick on bottom
        if abs(self.rect.midtop[1] - brick.rect.midbottom[1]) < 16:
            if self.__game.testing:
                print('brickbottomhit')
            self.velocity.y *= -1
            # self.rect.y += 8
            detected = True
        # Ball hits brick on left side
        if abs(self.rect.midright[0] - brick.rect.midleft[0]) < 16:
            if self.__game.testing:
                print('brickrighthit')
            self.velocity.x *= -1
            detected = True
        # Ball hits brick on right side
        if abs(self.rect.midleft[0] - brick.rect.midright[0]) < 16:
            if self.__game.testing:
                print('brickrighthit')
            self.velocity.x *= -1
            detected = True
        if not detected:
            if self.__game.testing:
                print('brick not detected :(')
        del self.__game.bricks[brickId]

    def paddleCollision(self, paddle):
        """ Checks the top left and right positions of the paddle and
        bottom left right positions of the ball giving a default state
        if no side is detected so the ball will never be stuck inside 
        the paddle
        """
        detected = False
        # Ball hits paddle on top
        if abs(self.rect.midbottom[1] - paddle.rect.midtop[1]) < 8:
            if self.__game.testing:
                print('tophit')
            self.velocity.y *= -1
            self.rect.bottom = paddle.rect.top - 4
            detected = True
        # Left side of paddle hits right side of ball
        if abs(self.rect.midright[0] - paddle.rect.midleft[0]) < 8:
            if self.__game.testing:
                print('lefthit')
            self.velocity.x *= -1
            if not detected:
                self.velocity.y *= -1
            self.rect.right = paddle.rect.left - 15
            detected = True
        # Right side of paddle hits left side of ball
        if abs(self.rect.midleft[0] - paddle.rect.midright[0]) < 8:
            if self.__game.testing:
                print('righthit')
            self.velocity.x *= -1
            if not detected:
                self.velocity.y *= -1
            self.rect.x = paddle.rect.midright[0]
            self.rect.left = paddle.rect.right + 15
            detected = True
        if not detected:
            if self.__game.testing:
                print('not detected / skimmed / it\'s a feature!')
            self.velocity.y *= -1
            self.rect.y -= abs(self.rect.midbottom[1] -
                               paddle.rect.midtop[1])

    def draw(self):
        # pygame.draw.rect(self.__game.screen, self.color, self.rect)
        self.__game.screen.blit(self.image, self.rect.topleft)
