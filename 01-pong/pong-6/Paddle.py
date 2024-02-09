import pygame
from config import *

class Paddle:
    # Class variables (Constants)
    # Paddle color: While for now
    COLOR = (255, 255, 255)
    # Paddle speed in units per second
    SPEED = 200

#--------------------------------------------------------------------------
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

#--------------------------------------------------------------------------
    
    def update(self, dt):
        '''
        This function checks whether the ball is about to leave the screen boundry.
        If so, it changes the direction of the ball.
           We know that if the user has pressed a key, the velocity will be non-zero.
           Otherwise if the user is not pressing any key, the velocity will be zero.
        '''
        
        # max here ensures that we're the greater of 0 or the player's current 
        # calculated Y position when pressing up so that we don't go into the 
        # negatives; the movement calculation is simply our previously-defined 
        # paddle speed scaled by dt
        if self.dy < 0:
            self.y = max(0, self.y + self.dy * dt)

        # similar to before, this time we use min to ensure we don't
        # go any farther than the bottom of the screen minus the paddle's
        # height (or else it will go partially below, since position is
        # based on its top left corner)
        else:
            self.y = min(VIRTUAL_HEIGHT - self.height, self.y + self.dy * dt)
        self.dy = 0

#--------------------------------------------------------------------------

    def moveUp(self):
        # Remember that the y-axis is positive downwards
        # Set -ve velocity to the paddle speed to move up
        self.dy = -Paddle.SPEED

#--------------------------------------------------------------------------
        
    def moveDown(self):
        # Remember that the y-axis is positive downwards
        # Set +ve velocity to the paddle speed to move down
        self.dy = Paddle.SPEED

#--------------------------------------------------------------------------
        
    def render(self, screen):
        '''
        Draw a rectangle on the screen
          Parameters:
          - screen: The surface to draw on
          - Paddle.COLOR: The color of the rectangle
          - (self.x, self.y, self.width, self.height): The position and dimensions of the rectangle
        '''
        pygame.draw.rect(screen, Paddle.COLOR, (self.x, self.y, self.width, self.height))
