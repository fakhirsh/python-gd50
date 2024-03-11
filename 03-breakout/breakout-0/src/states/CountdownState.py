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

class CountdownState(State):

    def load(self):
        self.hugeFont = pygame.font.Font('assets/fonts/flappy.ttf', 56)

        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')
        self.backgroundScroll = 0

        # ground image and starting scroll location (X axis)
        self.groundImg = pygame.image.load('assets/images/ground.png')
        self.groundScroll = 0

        self.counter = 3.99

        #print("CountdownState: load")

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        self.hugeFont   = None
        #print("CountdownState: unload")

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        #print("CountdownState: init")
        pass
        
    
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
        None

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        # Scroll background by preset speed * dt, looping back to 0 after the looping point
        self.backgroundScroll = (self.backgroundScroll + BACKGROUND_SCROLL_SPEED * dt) % BACKGROUND_LOOPING_POINT
        
        # Scroll ground by preset speed * dt, looping back to 0 after the screen width passes
        self.groundScroll = (self.groundScroll + GROUND_SCROLL_SPEED * dt) % VIRTUAL_WIDTH

        self.counter -= dt
        if self.counter < 1:
            from .PlayState import PlayState
            self.stateManager.changeState(PlayState())
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        
        # Draw the background at the negative looping point
        virtual_screen.blit(self.backgroundImg, (-self.backgroundScroll, 0))

        # Draw the ground on top of the background, toward the bottom of the screen,
        # at its negative looping point
        virtual_screen.blit(self.groundImg, (-self.groundScroll, VIRTUAL_HEIGHT - self.groundImg.get_height()))
        
        draw_text(str(int(self.counter)), self.hugeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT / 2, (255, 255, 255), virtual_screen)
        #print("TitleScreenState: render")

#--------------------------------------------------------------------------------------------------
