
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
from lib.Utils import *
from src.Global import Global
from src.states.StartState import StartState

class LoadState(State):
      
#--------------------------------------------------------------------------------------------------
        
    def load(self):
        assets = Global.assets
        # Fonts:
        assets['fonts']['medium'] = pygame.font.Font('assets/fonts/font.ttf', 16)

        # Sounds:
        assets['sounds']['clock'] = pygame.mixer.Sound('assets/sounds/clock.wav')
        assets['sounds']['error'] = pygame.mixer.Sound('assets/sounds/error.wav')
        assets['sounds']['game-over'] = pygame.mixer.Sound('assets/sounds/game-over.wav')
        assets['sounds']['match'] = pygame.mixer.Sound('assets/sounds/match.wav')
        assets['sounds']['music'] = pygame.mixer.Sound('assets/sounds/music.mp3')
        assets['sounds']['music2'] = pygame.mixer.Sound('assets/sounds/music2.mp3')
        assets['sounds']['music3'] = pygame.mixer.Sound('assets/sounds/music3.mp3')
        assets['sounds']['next-level'] = pygame.mixer.Sound('assets/sounds/next-level.wav')
        assets['sounds']['select'] = pygame.mixer.Sound('assets/sounds/select.wav')

        # Images:
        assets['images'] = {}
        assets['images']['background'] = pygame.image.load('assets/images/background.png')
        assets['images']['atlas'] = pygame.image.load('assets/images/match3.png')

        # # Quads:
        # self.assets['quads'] = {}
        # self.assets['quads']['paddle'] = GenerateQuadsPaddles()
        # self.assets['quads']['balls'] = GenerateQuadsBalls()
        # # Calculate the number of tiles in the spritesheet
        # sheet_width = self.assets['images']['atlas'].get_width() // TILE_WIDTH
        # sheet_height = self.assets['images']['atlas'].get_height() // TILE_HEIGHT
        # self.assets['quads']['bricks'] = GenerateQuadsBricks(sheet_width, sheet_height)

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
            Global.stateManager.changeState(StartState())
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, dt=0.0):
        # Clear the screen
        Global.virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        draw_text('Loading...', Global.assets['fonts']['large'], Global.VIRTUAL_WIDTH / 2, Global.VIRTUAL_HEIGHT/2, (255, 255, 255))

#--------------------------------------------------------------------------------------------------
