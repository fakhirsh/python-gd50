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

class Paddle:

    PADDLE_SPEED = 200
 
 #------------------------------------------------------------
       
    def __init__(self, atlas, quads):
        
        # start us off with no velocity
        self.dx = 0

        # the skin only has the effect of changing our color, used to offset us
        #   into the gPaddleSkins table later
        self.skin = 2
        # the variant is which of the four paddle sizes we currently are; 2
        #   is the starting size, as the smallest is too tough to start with
        self.size = 2

        # set the atlas and the quads
        self.atlas = atlas
        self.quads = quads
        # select appropriate quad based on skin and size
        self.rect = self.quads[self.size + 4 * (self.skin - 1)]
        print(self.rect)

        # starting dimensions
        self.width = self.rect.width
        self.height = self.rect.height

        # Set the paddle's initial position near the 
        #   bottom edge of the screen.
        self.x = VIRTUAL_WIDTH / 2 - self.width / 2
        self.y = VIRTUAL_HEIGHT - 32

#------------------------------------------------------------
        
    def update(self, dt):
        # keyboard input: continuous key press detection
        keys = pygame.key.get_pressed()
        self.dx = 0
        if keys[pygame.K_LEFT]:
            self.dx = -self.PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.dx = self.PADDLE_SPEED
        
        # If the paddle is moving to the left (negative dx), update the x position
        #   while ensuring it doesn't go beyond the left edge of the screen (0).
        if self.dx < 0:
            self.x = max(0, self.x + self.dx * dt)
        # If the paddle is moving to the right (positive dx), update the x position
        #   while ensuring it doesn't go beyond the right edge of the screen (VIRTUAL_WIDTH - self.width).
        else:
            self.x = min(VIRTUAL_WIDTH - self.width, self.x + self.dx * dt)

#------------------------------------------------------------
            
    def render(self, virtual_screen):
        # Draw the paddle at the given position
        virtual_screen.blit(self.atlas, (self.x, self.y), self.rect)

#------------------------------------------------------------