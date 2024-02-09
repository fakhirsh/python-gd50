'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

'''
Global constants for the game

WARNING:
    PLEASE NOTE that the way python namespaces work:
    Changing the value of a variable in one module will not change the value of the same variable in another module.

'''

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# Desired framerate
FPS = 60

WINNING_SCORE = 10

# Sound references
# FORCED to use dictionary instead of variables as changes to variables in one module
#  will not change the value of the same variable in another module
sounds = {
    'paddle_hit': None,
    'wall_hit': None,
    'point_scored': None
}