
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
from lib.Utils import draw_text
from src.Global import Global

class StartState(State):

    def load(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        # Play the music
        # -1 makes the music play indefinitely in a loop; use 0 to play it just once
        #pygame.mixer.music.play(-1)
        
        # currently selected menu item
        self.currentMenuItem = 1

        # colors we'll use to change the title text
        self.colors = {
            0: (217, 87,  99, 1),
            1: (95,  205, 228, 1),
            2: (251, 242, 54, 1),
            3: (118, 66,  138, 1),
            4: (153, 229, 80, 1),
            5: (223, 113, 38, 1)
        }

        # letters of MATCH 3 and their spacing relative to the center
        self.letterTable = [
            ['M', -108],
            ['A', -64],
            ['T', -28],
            ['C', 2],
            ['H', 40],
            ['3', 112]
        ]
        
        # keep track of scrolling our background on the X axis
        self.backgroundX = 0
    
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

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        # scroll background, used across all states
        self.backgroundX = self.backgroundX - Global.BACKGROUND_SCROLL_SPEED * dt

        # if we've scrolled the entire image, reset it to 0
        if self.backgroundX <= -1024 + Global.VIRTUAL_WIDTH - 4 + 51:
            self.backgroundX = 0
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, dt=0.0):
        
        # clear the screen
        Global.virtual_screen.fill((0, 0, 0))

        # draw the background starting at top left (0, 0)
        Global.virtual_screen.blit(Global.assets['images']['background'], (self.backgroundX, 0))

        # Draw the title of the game
        #draw_text('Match 3', Global.assets['fonts']['large'], Global.VIRTUAL_WIDTH / 2, Global.VIRTUAL_HEIGHT/3, (255, 255, 255))
        self.draw_match3_text(-60)

#--------------------------------------------------------------------------------------------------

    def draw_match3_text(self, y):
        # Assuming VIRTUAL_WIDTH, VIRTUAL_HEIGHT, and self.colors are defined elsewhere in the class
        # pygame doesn't support directly setting alpha on surfaces, so we create an alpha surface
        #screen = pygame.display.get_surface()  # Get the current display surface
        
        # Draw semi-transparent rect behind MATCH 3
        alpha_surf = pygame.Surface((150, 58), pygame.SRCALPHA)  # Create a transparent surface
        alpha_surf.fill((255, 255, 255, 128))  # Fill the surface with a semi-transparent color
        Global.virtual_screen.blit(alpha_surf, (Global.VIRTUAL_WIDTH / 2 - 76, Global.VIRTUAL_HEIGHT / 2 + y - 11))
        
        # Assuming the method draw_text_shadow and the font have been defined elsewhere
        self.draw_text_shadow('MATCH 3', Global.VIRTUAL_HEIGHT / 2 + y)
        
        # Print MATCH 3 letters in their corresponding current colors
        for i in range(6):
            color = self.colors[i]  # Assuming self.colors is a list of RGB color tuples
            # Assuming self.letter_table is structured similarly to self.letterTable in Lua
            letter, offset = self.letterTable[i]
            text_surface = Global.assets['fonts']['large'].render(letter, True, color)  # Render the text
            # Calculate the x position based on the offset
            x_pos = (Global.VIRTUAL_WIDTH + offset) / 2 - text_surface.get_width() / 2
            Global.virtual_screen.blit(text_surface, (x_pos, Global.VIRTUAL_HEIGHT / 2 + y))

#--------------------------------------------------------------------------------------------------
            
    def draw_text_shadow(self, text, y):
        color = (34, 32, 52, 1)
        font = Global.assets['fonts']['large']
        text_surface = font.render(text, True, color)
        x_pos = Global.VIRTUAL_WIDTH / 2 - text_surface.get_width() / 2
        Global.virtual_screen.blit(text_surface, (x_pos + 2, y + 1))
        Global.virtual_screen.blit(text_surface, (x_pos + 1, y + 1))
        Global.virtual_screen.blit(text_surface, (x_pos, y + 1))
        Global.virtual_screen.blit(text_surface, (x_pos + 1, y + 2))