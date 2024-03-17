'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from src.Global import Global

def draw_text(text, font, x, y, color):
    '''
    In PyGame, text is drawn in two steps:
      1. Render the text on a temporary surface
      2. Draw the text surface on the screen buffer
    '''
    # Render the text on a temporary surface
    text_surface = font.render(text, True, color)
    
    # Get the rectangle of the text surface. Also, 
    #   Center the text at (x, y).
    #   If we don't center the text, then the default position 
    #     is at the top left corner of the text surface
    text_rect = text_surface.get_rect(center=(x, y))
    
    # Finally draw the text surface on the given screen buffer
    Global.virtual_screen.blit(text_surface, text_rect)


def display_fps(fpsValue):
    # simple FPS display across all states
    # The render function takes the following parameters:
    #   - The text to render
    #   - Anti-aliasing: True or False
    #   - The color of the text
    font = Global.assets['fonts']['small']
    fps_text = font.render('FPS: ' + str(fpsValue), True, (0, 255, 0))
    
    # Finally draw the text surface on the virtual screen buffer
    Global.virtual_screen.blit(fps_text, (5, 5))

#------------------------------------------------------------

'''
    Given an "atlas" (a texture with multiple sprites), as well as a
    width and a height for the tiles therein, split the texture into
    all of the quads by simply dividing it evenly.
'''
def GenerateQuads(sheet_width, sheet_height, tilewidth, tileheight):
    
    # Create an empty list to store the sprite rectangles
    spritesheet = []

    # Iterate over each row and column in the spritesheet
    for y in range(sheet_height):
        for x in range(sheet_width):
            # Create a rectangle for the current sprite
            sprite_rect = pygame.Rect(x * tilewidth, y * tileheight, tilewidth, tileheight)
            # Add the sprite rectangle to the list
            spritesheet.append(sprite_rect)

    # Return the list of sprite rectangles
    return spritesheet

#------------------------------------------------------------
