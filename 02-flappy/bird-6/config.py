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

# The horizontal scroll speed of the pipe
PIPE_SCROLL = -60
# The size of the gap between two pipes in a pair of pipes
GAP_HEIGHT = 90
# Width and height of the pipe image
PIPE_HEIGHT = 288
PIPE_WIDTH = 70
# The minimum and maximum possible variation from the previous pipe's Y position
PIPE_Y_VARIATION = 40
