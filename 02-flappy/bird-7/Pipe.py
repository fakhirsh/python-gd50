import random
import pygame
from config import *

class Pipe:
#-----------------------------------------------------
    
    def __init__(self, orientation, y):
        # Load the pipe image.
        self.image = pygame.image.load('assets/images/pipe.png')
        # If the pipe is at the top, flip the image vertically.
        if orientation == 'top':
            self.image = pygame.transform.flip(self.image, False, True)

        # Store the width and height of the pipe.
        self.width, self.height = self.image.get_size()

        # Set the horizontal position of the pipe outside the left edge of the screen.
        self.x = VIRTUAL_WIDTH
        # Set the vertical position of the pipe to the specified y position.
        self.y = y
        # Orientation: Whether the pipe is at the top or bottom.
        self.orientation = orientation

#-----------------------------------------------------
        
    def update(self, dt):
        # Pipe pair is actually moving both pipes so no need to update the pipe position here.
        pass

#-----------------------------------------------------
    
    def render(self, screen):
        # Draw the pipe at the specified position.
        screen.blit(self.image, (self.x, self.y))

#-----------------------------------------------------