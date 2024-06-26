'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame

class Brick:
    def __init__(self, x, y, atlas, brickQuads):
        
        self.atlas = atlas
        self.brickQuads = brickQuads
        
        # used for coloring and score calculation
        self.tier = 0
        self.color = 0
                
        self.rect = self.brickQuads[self.color + self.tier * 4]

        self.x = x
        self.y = y
        self.width = 32
        self.height = 16
        
        # used to determine whether this brick should be rendered
        self.inPlay = True

        self.brickHitSound = pygame.mixer.Sound('assets/sounds/brick-hit-2.wav')

#------------------------------------------------------------
        
    def hit(self):
        # Sound on hit
        self.brickHitSound.play()
        # Set the brick to be inactive
        self.inPlay = False

#------------------------------------------------------------
        
    def render(self, virtual_screen):
        # Draw the brick if it's in play
        if self.inPlay:
            virtual_screen.blit(self.atlas, (self.x, self.y), self.rect)

#------------------------------------------------------------