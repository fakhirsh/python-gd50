import random
import pygame
from config import *
import random

class Ball:
    # Class variable. White color for now
    COLOR = (255, 255, 255)

#--------------------------------------------------------------------------
    
    def __init__(self, x, y, width, height, paddle1, paddle2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Randomize the direction of the ball both in x and y axis
        self.dx = -100 if random.randint(1, 2) == 1 else 100
        self.dy = random.randint(-100, -80) if random.randint(1, 2) == 1 else random.randint(80, 100)
        
        # Save the paddles to check collision
        self.paddle1 = paddle1
        self.paddle2 = paddle2

#--------------------------------------------------------------------------

    def reset(self):
        # Reset the ball to the center of the screen
        self.x = VIRTUAL_WIDTH // 2
        self.y = VIRTUAL_HEIGHT // 2
       
        # Randomize the direction of the ball both in x and y axis
        self.dx = -100 if random.randint(1, 2) == 1 else 100
        self.dy = random.randint(-100, -80) if random.randint(1, 2) == 1 else random.randint(80, 100)

#--------------------------------------------------------------------------

    def update(self, dt):
        '''
        This function moves the ball and checks for collision with the screen boundries and paddles
        '''
        
        # Move the ball based on the direction and time passed
        self.x += self.dx * dt
        self.y += self.dy * dt
        
        # Check collision with screen boundries (top)
        if self.y <= 0:
        
            # Reset the position and change the direction
            self.y = 0
            self.dy = -self.dy
        
        # Check collision with bottom edge
        elif self.y >= VIRTUAL_HEIGHT - self.height:
        
            # Reset the position and change the direction
            self.y = VIRTUAL_HEIGHT - self.height
            self.dy = -self.dy

        # Check collision with the first paddle
        if self.checkCollision(self.paddle1):
        
            # Reset the position and change the direction
            self.x = self.paddle1.x + self.paddle1.width
        
            # Increase the speed of the ball by 3% every time it hits the paddle
            self.dx = -self.dx * 1.03
        
            # Impact the y direction of the ball based on the paddle movement
            self.dy += self.paddle1.dy / 4
        
        # Check collision with the second paddle
        elif self.checkCollision(self.paddle2):
            
            # Reset the position and change the direction
            self.x = self.paddle2.x - self.width
            
            # Increase the speed of the ball by 3% every time it hits the paddle
            self.dx = -self.dx * 1.03
            
            # Impact the y direction of the ball based on the paddle movement
            self.dy += self.paddle2.dy / 4

#--------------------------------------------------------------------------
            
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

#--------------------------------------------------------------------------
 
    def render(self, screen):
        '''
        This function renders the ball on the screen
        '''
        pygame.draw.rect(screen, Ball.COLOR, (self.x, self.y, self.width, self.height))

    