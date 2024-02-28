'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

# Desired framerate
FPS = 60

# Speed at which we should scroll our images, scaled by dt
BACKGROUND_SCROLL_SPEED = 30
GROUND_SCROLL_SPEED = 60

# Point at which we should loop our background back to X 0
BACKGROUND_LOOPING_POINT = 413

# Gravity to apply to our bird
GRAVITY = 20