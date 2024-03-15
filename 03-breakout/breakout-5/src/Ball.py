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
       
    def __init__(self, assets, paddle):  
        self.assets = assets
        # set the atlas and the quads
        self.atlas = self.assets['images']['atlas']
        self.ballQuads = self.assets['quads']['balls']

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
            pygame.mixer.Sound.play(self.assets['sounds']['wall_hit'])

        if self.x >= VIRTUAL_WIDTH - 8:
            self.x = VIRTUAL_WIDTH - 8
            self.dx = -self.dx
            pygame.mixer.Sound.play(self.assets['sounds']['wall_hit'])

        if self.y <= 0:
            self.y = 0
            self.dy = -self.dy
            pygame.mixer.Sound.play(self.assets['sounds']['wall_hit'])

        if self.checkCollision(self.paddle):
            self.dy = -self.dy
            pygame.mixer.Sound.play(self.assets['sounds']['paddle_hit'])
 
            # tweak angle of bounce based on where it hits the paddle

            # if we hit the paddle on its left side while moving left...
            if self.x < self.paddle.x + (self.paddle.width / 2) and self.paddle.dx < 0:
                self.dx = -50 + -(8 * (self.paddle.x + self.paddle.width / 2 - self.x))
                # ensure that the ball is always moving upwards even if it hits at very steep side angles
                self.dy = -self.dy if self.dy > 0 else self.dy

            # else if we hit the paddle on its right side while moving right...
            elif self.x > self.paddle.x + (self.paddle.width / 2) and self.paddle.dx > 0:
                self.dx = 50 + (8 * abs(self.paddle.x + self.paddle.width / 2 - self.x))
                # ensure that the ball is always moving upwards even if it hits at very steep side angles
                self.dy = -self.dy if self.dy > 0 else self.dy
                
#------------------------------------------------------------
            
    def render(self, virtual_screen):
        # Draw the paddle at the given position
        virtual_screen.blit(self.atlas, (self.x, self.y), self.rect)

#------------------------------------------------------------
        
    def checkCollision(self, rect):
        '''
        This function checks if the ball is colliding with a rectangle
        '''
        
        # First, check to see if the left edge of either is farther to the right
        # than the right edge of the other
        if self.x > rect.x + rect.width or self.x + self.width < rect.x:
            return False
        
        # Then check to see if the bottom edge of either is higher than the top
        # edge of the other
        if self.y > rect.y + rect.height or self.y + self.height < rect.y:
            return False
        
        # if the above aren't true, they're overlapping
        return True
    
#------------------------------------------------------------
