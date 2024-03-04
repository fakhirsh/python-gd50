'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

from config import *
from Pipe import Pipe

class PipePair:

#-----------------------------------------------------
    
    def __init__(self, y):
        # Set the horizontal position of the pipe pair outside the right edge of the screen.
        self.x = VIRTUAL_WIDTH + 32
        # Set the vertical position of the pipe pair to the specified y position.
        self.y = y
        # Create two pipes that make up the pair.
        self.pipes = {
            'upper': Pipe('top', self.y - PIPE_HEIGHT - GAP_HEIGHT),
            'lower': Pipe('bottom', self.y)
        }
        # This variable checks if the pipe pair should be removed from the scene.
        #  It is set to True when the pipe pair is off the left edge of the screen.
        self.remove = False

#-----------------------------------------------------

    def update(self, dt):

        """
        This function updates the position of the pipe pair based on the elapsed time (dt).
        If the pipe pair is still within the screen boundaries, it moves the pair to the left.
        It also updates the x position of the upper and lower pipes to match the new position of the pipe pair.
        If the pipe pair has moved off the left edge of the screen, it sets the remove variable to True.
        """

        # If the pipe pair is still within the screen boundaries, move the pair to the left.
        if self.x > -PIPE_WIDTH:
            self.x += PIPE_SCROLL * dt
            # Update the x position of the upper and lower pipes to match the new position of the pipe pair.
            self.pipes['upper'].x = int(self.x)
            self.pipes['lower'].x = int(self.x)
        else:
            # If the pipe pair has moved off the left edge of the screen, set the remove variable to True.
            self.remove = True

#-----------------------------------------------------

    def render(self, dt):
        # Render the upper and lower pipes in the pipe pair.
        for pipe in self.pipes.values():
            pipe.render(dt)

#-----------------------------------------------------