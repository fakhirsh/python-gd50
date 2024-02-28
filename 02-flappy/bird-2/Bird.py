import pygame
from config import *

class Bird:
    '''
    This class represents the bird.
    '''
    def __init__(self):
        '''
        Constructor for the Bird class.
        '''
        # Load the bird image.
        self.image = pygame.image.load('assets/images/bird.png')
        
        # Store the width and height of the bird.
        self.width, self.height = self.image.get_size()
        
        # Set the bird's initial position to the center of the screen.
        self.x = VIRTUAL_WIDTH / 2 - self.width / 2
        self.y = VIRTUAL_HEIGHT / 2 - self.height / 2

    def render(self, screen):
        '''
        Draw the bird on the screen.
        '''
        screen.blit(self.image, (self.x, self.y))