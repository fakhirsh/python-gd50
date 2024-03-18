'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from config import *

class Bird:

#-----------------------------------------------------
    
    def __init__(self):
        '''
        Constructor for the Bird class.
        '''
        # Load the bird image.
        self.image = pygame.image.load('assets/images/bird.png')
        
        # Store the width and height of the bird.
        self.width, self.height = self.image.get_size()
        
        # Set the bird's initial position to the center of the screen.
        self.x = 0
        self.y = 0
        self.duration = 0
        self.opacity = 255
        self.angle = 0

#-----------------------------------------------------

    def update(self, dt):
        pass

#-----------------------------------------------------

    def render(self, screen):
        '''
        Draw the bird on the screen.
        '''
        # Rotate the image around its center
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)

        temp_surface = rotated_image.copy()
        temp_surface.set_alpha(self.opacity)
        screen.blit(temp_surface, new_rect.topleft)

#-----------------------------------------------------