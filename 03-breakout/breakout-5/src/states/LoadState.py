
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
from lib.utils import *
from src.config import *
from src.states.StartState import StartState

class LoadState(State):

    def __init__(self, assets):
        self.assets = assets
        
#--------------------------------------------------------------------------------------------------
        
    def load(self):
        # Fonts:
        self.assets['fonts']['medium'] = pygame.font.Font('assets/fonts/font.ttf', 16)

        # Sounds:
        self.assets['sounds']['paddle_hit'] = pygame.mixer.Sound('assets/sounds/paddle_hit.wav')
        self.assets['sounds']['confirm'] = pygame.mixer.Sound('assets/sounds/confirm.wav')
        self.assets['sounds']['wall_hit'] = pygame.mixer.Sound('assets/sounds/wall_hit.wav')
        self.assets['sounds']['brick_hit'] = pygame.mixer.Sound('assets/sounds/brick-hit-2.wav')
        self.assets['sounds']['victory'] = pygame.mixer.Sound('assets/sounds/victory.wav')
        self.assets['sounds']['pause'] = pygame.mixer.Sound('assets/sounds/pause.wav')

        # Images:
        self.assets['images'] = {}
        self.assets['images']['background'] = pygame.image.load('assets/images/background.png')
        self.assets['images']['atlas'] = pygame.image.load('assets/images/breakout.png')

        # Quads:
        self.assets['quads'] = {}
        self.assets['quads']['paddle'] = GenerateQuadsPaddles()
        self.assets['quads']['balls'] = GenerateQuadsBalls()
        # Calculate the number of tiles in the spritesheet
        sheet_width = self.assets['images']['atlas'].get_width() // TILE_WIDTH
        sheet_height = self.assets['images']['atlas'].get_height() // TILE_HEIGHT
        self.assets['quads']['bricks'] = GenerateQuadsBricks(sheet_width, sheet_height)

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        self.timer = 0.0
        
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
        pass

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.stateManager.changeState(StartState(self.assets))
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # Clear the screen
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        draw_text('Loading...', self.assets['fonts']['large'], VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2, (255, 255, 255), virtual_screen)

#--------------------------------------------------------------------------------------------------
