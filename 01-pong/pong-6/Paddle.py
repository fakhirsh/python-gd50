import pygame
from config import *

class Paddle:
    COLOR = (255, 255, 255)
    # paddle speed in units per second
    SPEED = 200
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.score = 0

    def update(self, dt):
        if self.dy < 0:
            self.y = max(0, self.y + self.dy * dt)
        else:
            self.y = min(VIRTUAL_HEIGHT - self.height, self.y + self.dy * dt)
        self.dy = 0

    def moveUp(self):
        self.dy = -Paddle.SPEED
    
    def moveDown(self):
        self.dy = Paddle.SPEED

    def render(self, screen):
        pygame.draw.rect(screen, Paddle.COLOR, (self.x, self.y, self.width, self.height))
