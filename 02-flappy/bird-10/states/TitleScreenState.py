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

class TitleScreenState(State):

    def load(self):
        # initialize our nice-looking retro text fonts
        self.small_font = pygame.font.Font('assets/fonts/font.ttf', 8)
        self.mediumFont = pygame.font.Font('assets/fonts/flappy.ttf', 14)
        self.flappyFont = pygame.font.Font('assets/fonts/flappy.ttf', 28)
        self.hugeFont   = pygame.font.Font('assets/fonts/flappy.ttf', 56)

        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')
        self.backgroundScroll = 0

        # ground image and starting scroll location (X axis)
        self.groundImg = pygame.image.load('assets/images/ground.png')
        self.groundScroll = 0

        print("TitleScreenState: load")

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        self.small_font = None
        self.mediumFont = None
        self.flappyFont = None
        self.hugeFont   = None
        print("TitleScreenState: unload")

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        print("TitleScreenState: init")
        
    
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
        # Scroll background by preset speed * dt, looping back to 0 after the looping point
        self.backgroundScroll = (self.backgroundScroll + BACKGROUND_SCROLL_SPEED * dt) % BACKGROUND_LOOPING_POINT
        
        # Scroll ground by preset speed * dt, looping back to 0 after the screen width passes
        self.groundScroll = (self.groundScroll + GROUND_SCROLL_SPEED * dt) % VIRTUAL_WIDTH
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
         # Clear the virtual screen
        #virtual_screen.fill((0, 0, 0))
        
        # Draw the background at the negative looping point
        virtual_screen.blit(self.backgroundImg, (-self.backgroundScroll, 0))

        # Draw the ground on top of the background, toward the bottom of the screen,
        # at its negative looping point
        virtual_screen.blit(self.groundImg, (-self.groundScroll, VIRTUAL_HEIGHT - self.groundImg.get_height()))
        
        draw_text('FC Bird', self.flappyFont, VIRTUAL_WIDTH / 2, 64, (255, 255, 255), virtual_screen)
        draw_text('Press Enter', self.mediumFont, VIRTUAL_WIDTH / 2, 100, (255, 255, 255), virtual_screen)
        #print("TitleScreenState: render")

#--------------------------------------------------------------------------------------------------
