import random
import pygame
from config import *

class Pipe:
    def __init__(self):
        # Load the pipe image.
        self.image = pygame.image.load('assets/images/pipe.png')
        # Store the width and height of the pipe.
        self.width, self.height = self.image.get_size()

        self.x = VIRTUAL_WIDTH
        self.y = random.randint(VIRTUAL_HEIGHT // 4, VIRTUAL_HEIGHT - 10)


    def update(self, dt):
        self.x += PIPE_SCROLL * dt


    def render(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))
