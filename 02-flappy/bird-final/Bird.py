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
        self.jumpSound = pygame.mixer.Sound('assets/sounds/jump.wav')

        # Store the width and height of the bird.
        self.width, self.height = self.image.get_size()
        
        # Set the bird's initial position to the center of the screen.
        self.x = VIRTUAL_WIDTH / 2 - self.width / 2
        self.y = VIRTUAL_HEIGHT / 2 - self.height / 2
        
        # Y velocity; gravity
        self.dy = 0

#-----------------------------------------------------

    def update(self, dt):
        '''
        Update the bird's position.
        '''
        # Apply gravity to the bird's velocity.
        self.dy = self.dy + GRAVITY * dt
        
        # Update the bird's y-position.
        self.y = self.y + self.dy

#-----------------------------------------------------

    def applyForce(self):
        '''
        Apply a force to the bird.
        '''
        self.dy = -5
        self.jumpSound.play()

#-----------------------------------------------------

    def render(self, screen):
        '''
        Draw the bird on the screen.
        '''
        screen.blit(self.image, (self.x, self.y))

        # For debugging: draw a bounding box around the bird
        # pygame.draw.rect(screen, (0,255,0), (self.x, self.y, self.width, self.height), width=1)

#-----------------------------------------------------

    def collides(self, pipe):
        '''
        AABB collision that expects a pipe, which will have an X and Y and reference
        global pipe width and height values.
        '''
        # The 2's are left and top offsets
        # The 4's are right and bottom offsets
        # Both offsets are used to shrink the bounding box to give the player
        #    a little bit of leeway with the collision
        if (self.x + 2) + (self.width - 4) >= pipe.x and self.x + 2 <= pipe.x + PIPE_WIDTH:
            if (self.y + 2) + (self.height - 4) >= pipe.y and self.y + 2 <= pipe.y + PIPE_HEIGHT:
                return True

        return False

#-----------------------------------------------------