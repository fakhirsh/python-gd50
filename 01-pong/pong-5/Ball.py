import random
import pygame
from config import *

class Ball:
    COLOR = (255, 255, 255)
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = 100 if random.randint(1, 2) == 1 else -100
        self.dy = random.randint(-50, 50) 

    def reset(self):
        self.x = VIRTUAL_WIDTH // 2
        self.y = VIRTUAL_HEIGHT // 2
        self.dx = 100 if random.randint(1, 2) == 1 else -100
        self.dy = random.randint(-50, 50) 

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        
    def render(self, screen):
        pygame.draw.rect(screen, Ball.COLOR, (self.x, self.y, self.width, self.height))

    