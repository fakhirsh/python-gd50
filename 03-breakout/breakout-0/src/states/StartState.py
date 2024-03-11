
'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from .State import State
from lib.utils import draw_text
from src.config import *

class StartState(State):

    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.smallFont = pygame.font.Font('assets/fonts/font.ttf', 8)
        self.mediumFont = pygame.font.Font('assets/fonts/font.ttf', 16)
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)
        
        self.paddleHit = pygame.mixer.Sound('assets/sounds/paddle_hit.wav')

        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')
        self.backgroundScroll = 0

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        # initialize the highlighted menu item
        self.highlighted = 1
        
    
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the return key
                pass
            elif event.key == pygame.K_UP:
                # Handle the up arrow key
                self.highlighted = 1
                self.paddleHit.play()
            elif event.key == pygame.K_DOWN:
                # Handle the down arrow key
                self.highlighted = 2
                self.paddleHit.play()

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        
        background_width, background_height = self.backgroundImg.get_size()

        # Scaling the background image
        # First we calculate the scale factor
        scale_x = VIRTUAL_WIDTH / (background_width - 1)
        scale_y = VIRTUAL_HEIGHT / (background_height - 1)
        # Then we create a new background with the new scaled dimensions
        scaled_background = pygame.transform.scale(self.backgroundImg, (int(background_width * scale_x), int(background_height * scale_y)))

        # Drawing the scaled image at coordinates (0, 0)
        virtual_screen.blit(scaled_background, (0, 0))

        # Draw the title of the game
        draw_text('BREAKOUT', self.largeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/3, (255, 255, 255), virtual_screen)
        
        # Set the default color for the menu items
        color = (255, 255, 255)
        # Check if the first menu item is highlighted
        if self.highlighted == 1:
            # Change the color to indicate that it is highlighted
            color = (103, 255, 255)
        # Draw the 'START' menu item
        draw_text('START', self.mediumFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2+70, color, virtual_screen)
        # Reset the color to the default
        color = (255, 255, 255)
        # Check if the second menu item is highlighted
        if self.highlighted == 2:
            # Change the color to indicate that it is highlighted
            color = (103, 255, 255)
        # Draw the 'HIGH SCORES' menu item
        draw_text('HIGH SCORES', self.mediumFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2+90, color, virtual_screen)

#--------------------------------------------------------------------------------------------------
