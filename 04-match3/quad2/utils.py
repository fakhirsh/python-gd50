'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame

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
    for y in range(sheet_height//tileheight):
        for x in range(sheet_width//tilewidth):
            # Create a rectangle for the current sprite
            sprite_rect = pygame.Rect(x * tilewidth, y * tileheight, tilewidth, tileheight)
            # Add the sprite rectangle to the list
            spritesheet.append(sprite_rect)

    # Return the list of sprite rectangles
    return spritesheet

#------------------------------------------------------------

