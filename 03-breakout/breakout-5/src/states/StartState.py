
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
from src.states.PlayState import PlayState

class StartState(State):
    def __init__(self, assets):
        self.assets = assets

    def load(self):
        pass

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
                if self.highlighted == 1:
                    # Start the game
                    self.assets['sounds']['confirm'].play()
                    self.stateManager.changeState(PlayState(self.assets))
                elif self.highlighted == 2:
                    # Show the high scores
                    self.assets['sounds']['confirm'].play()
                    #self.stateManager.changeState(HighScoreState(self.assets))
            elif event.key == pygame.K_UP:
                # Handle the up arrow key
                self.highlighted = 1
                self.assets['sounds']['paddle_hit'].play()
            elif event.key == pygame.K_DOWN:
                # Handle the down arrow key
                self.highlighted = 2
                self.assets['sounds']['paddle_hit'].play()

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        
        background_width, background_height = self.assets['images']['background'].get_size()

        # Scaling the background image
        # First we calculate the scale factor
        scale_x = VIRTUAL_WIDTH / (background_width - 1)
        scale_y = VIRTUAL_HEIGHT / (background_height - 1)
        # Then we create a new background with the new scaled dimensions
        scaled_background = pygame.transform.scale(self.assets['images']['background'], (int(background_width * scale_x), int(background_height * scale_y)))

        # Drawing the scaled image at coordinates (0, 0)
        virtual_screen.blit(scaled_background, (0, 0))

        # Draw the title of the game
        draw_text('BREAKOUT', self.assets['fonts']['large'], VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/3, (255, 255, 255), virtual_screen)
        
        # Set the default color for the menu items
        color = (255, 255, 255)
        # Check if the first menu item is highlighted
        if self.highlighted == 1:
            # Change the color to indicate that it is highlighted
            color = (103, 255, 255)
        # Draw the 'START' menu item
        draw_text('START', self.assets['fonts']['medium'], VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2+70, color, virtual_screen)
        # Reset the color to the default
        color = (255, 255, 255)
        # Check if the second menu item is highlighted
        if self.highlighted == 2:
            # Change the color to indicate that it is highlighted
            color = (103, 255, 255)
        # Draw the 'HIGH SCORES' menu item
        draw_text('HIGH SCORES', self.assets['fonts']['medium'], VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2+90, color, virtual_screen)

#--------------------------------------------------------------------------------------------------
