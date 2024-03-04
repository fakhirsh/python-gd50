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
from utils import draw_text
from config import *

class ScoreState(State):

    def __init__(self, params):
        self.score = params['score']
        print("ScoreState: __init__")

    def load(self):
        # initialize our nice-looking retro text fonts
        self.small_font = pygame.font.Font('assets/fonts/font.ttf', 8)
        self.mediumFont = pygame.font.Font('assets/fonts/flappy.ttf', 14)
        self.flappyFont = pygame.font.Font('assets/fonts/flappy.ttf', 28)
        self.hugeFont   = pygame.font.Font('assets/fonts/flappy.ttf', 56)

        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')

        # ground image and starting scroll location (X axis)
        self.groundImg = pygame.image.load('assets/images/ground.png')

        print("ScoreState: load")

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        self.small_font = None
        self.mediumFont = None
        self.flappyFont = None
        self.hugeFont   = None
        print("ScoreState: unload")

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        print("ScoreState: init")
        
    
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
                from .CountdownState import CountdownState
                self.stateManager.changeState(CountdownState())
                # Transition to another state or perform other actions

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
         # Clear the virtual screen
        #virtual_screen.fill((0, 0, 0))
        
        # Draw the background at the negative looping point
        virtual_screen.blit(self.backgroundImg, (0, 0))

        # Draw the ground on top of the background, toward the bottom of the screen,
        # at its negative looping point
        virtual_screen.blit(self.groundImg, (0, VIRTUAL_HEIGHT - self.groundImg.get_height()))
        
        draw_text('Oof! You lost!', self.flappyFont, VIRTUAL_WIDTH / 2, 64, (255, 255, 255), virtual_screen)
        draw_text('Score: ' + str(self.score), self.mediumFont, VIRTUAL_WIDTH / 2, 100, (255, 255, 255), virtual_screen)
        draw_text('Press Enter to Play Again!', self.mediumFont, VIRTUAL_WIDTH / 2, 160, (255, 255, 255), virtual_screen)

#--------------------------------------------------------------------------------------------------
