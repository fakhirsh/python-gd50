import random
import pygame
from config import *
import random

class Ball:
    # Class variable. White color for now
    COLOR = (255, 255, 255)

#--------------------------------------------------------------------------
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Randomize the direction of the ball both in x and y axis
        self.dx = 100 if random.randint(1, 2) == 1 else -100
        self.dy = random.randint(-50, 50) 
        
#--------------------------------------------------------------------------

    def reset(self):
        # Reset the ball to the center of the screen
        self.x = VIRTUAL_WIDTH // 2
        self.y = VIRTUAL_HEIGHT // 2
       
        # Randomize the direction of the ball both in x and y axis
        self.dx = 100 if random.randint(1, 2) == 1 else -100
        self.dy = random.randint(-50, 50) 

#--------------------------------------------------------------------------

    def update(self, dt):
        '''
        This function moves the ball and checks for collision with the screen boundries and paddles
        '''
        
        # Move the ball based on the direction and time passed
        self.x += self.dx * dt
        self.y += self.dy * dt

#--------------------------------------------------------------------------
 
    def render(self, screen):
        '''
        This function renders the ball on the screen
        '''
        pygame.draw.rect(screen, Ball.COLOR, (self.x, self.y, self.width, self.height))

    