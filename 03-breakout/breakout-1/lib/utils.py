'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame

def draw_text(text, font, x, y, color, screen):
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
    screen.blit(text_surface, text_rect)


def display_fps(virtual_screen, font, fpsValue):
    # simple FPS display across all states
    # The render function takes the following parameters:
    #   - The text to render
    #   - Anti-aliasing: True or False
    #   - The color of the text
    fps_text = font.render('FPS: ' + str(fpsValue), True, (0, 255, 0))
    
    # Finally draw the text surface on the virtual screen buffer
    virtual_screen.blit(fps_text, (10, 10))

#------------------------------------------------------------

def GenerateQuads(atlas, tilewidth, tileheight):
    # Calculate the number of tiles in the spritesheet
    sheet_width = atlas.get_width() // tilewidth
    sheet_height = atlas.get_height() // tileheight

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

def GenerateQuadsPaddles(atlas):
    x = 0
    y = 64

    quads = []
    for i in range(4):
        # smallest paddle
        quads.append(pygame.Rect(x, y, 32, 16))
        # medium paddle
        quads.append(pygame.Rect(x + 32, y, 64, 16))
        # large paddle
        quads.append(pygame.Rect(x + 96, y, 96, 16))
        # huge paddle
        quads.append(pygame.Rect(x, y + 16, 128, 16))

        # Prepare X and Y for the next set of paddles
        y += 32

    return quads

#------------------------------------------------------------