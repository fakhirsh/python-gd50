'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from src.config import *
import random

class Ball:

    BALL_SPEED = 200
 
 #------------------------------------------------------------
       
    def __init__(self, atlas, ballQuads, paddle):  
        # set the atlas and the quads
        self.atlas = atlas
        self.ballQuads = ballQuads

        # Ball skin ranges from 0 to 6
        self.skin = random.randint(0, 6)
        # Select appropriate ball skin
        self.rect = self.ballQuads[self.skin]

        # starting dimensions
        self.width = self.rect.width
        self.height = self.rect.height
        # Save the paddles to check collision
        self.paddle = paddle

        # Reset the ball to the center of the screen
        self.reset()

        self.wallHitSound = pygame.mixer.Sound('assets/sounds/wall_hit.wav')
        self.paddleHitSound = pygame.mixer.Sound('assets/sounds/paddle_hit.wav')
#------------------------------------------------------------

    def reset(self):
        # Reset the ball to the center of the screen
        self.x = VIRTUAL_WIDTH // 2 - self.width/2
        self.y = VIRTUAL_HEIGHT - 42
       
        self.dx = 0
        self.dy = 0

#------------------------------------------------------------

    def update(self, dt):
        # In the ready state, just before the gameplay has begun
        #    the ball should move with the paddle
        # self.x = self.paddle.x + (self.paddle.width - self.width) / 2

        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt

        # allow ball to bounce off walls
        if self.x <= 0:
            self.x = 0
            self.dx = -self.dx
            pygame.mixer.Sound.play(self.wallHitSound)

        if self.x >= VIRTUAL_WIDTH - 8:
            self.x = VIRTUAL_WIDTH - 8
            self.dx = -self.dx
            pygame.mixer.Sound.play(self.wallHitSound)

        if self.y <= 0:
            self.y = 0
            self.dy = -self.dy
            pygame.mixer.Sound.play(self.wallHitSound)

        if self.checkCollision():
            self.dy = -self.dy
            pygame.mixer.Sound.play(self.paddleHitSound)
 
#------------------------------------------------------------
            
    def render(self, virtual_screen):
        # Draw the paddle at the given position
        virtual_screen.blit(self.atlas, (self.x, self.y), self.rect)

#------------------------------------------------------------
        
    def checkCollision(self):
        '''
        This function checks if the ball is colliding with a rectangle
        '''
        
        # First, check to see if the left edge of either is farther to the right
        # than the right edge of the other
        if self.x > self.paddle.x + self.paddle.width or self.x + self.width < self.paddle.x:
            return False
        
        # Then check to see if the bottom edge of either is higher than the top
        # edge of the other
        if self.y > self.paddle.y + self.paddle.height or self.y + self.height < self.paddle.y:
            return False
        
        # if the above aren't true, they're overlapping
        return True
    
#------------------------------------------------------------
