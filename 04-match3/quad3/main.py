'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
import sys
from utils import *
import random

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

# Desired framerate
FPS = 60

#---------------------------------------------------------

virtual_screen = None
window = None
clock = None

#---------------------------------------------------------

# Global game state variables
matchImg = None
quads = []

# tweening variable
timer = 0
#---------------------------------------------------------

def load():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''

    global window, virtual_screen, clock, matchImg, quads


    # Initialize pygame
    pygame.init()

    # Create game window of size WINDOW_WIDTH x WINDOW_HEIGHT
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Set window title
    pygame.display.set_caption('tween0')
    
    # Create a virtual screen to draw on before scaling to the window size
    #  Basically we want to draw everything on a smaller screen and then 
    #  scale it up to the window size
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

    # The Clock object is responsible for keeping track of time and 
    # regulating the frame rate. It provides methods like tick() to 
    # control the frame rate and measure the time between frames.
    clock = pygame.time.Clock()


#---------------------------------------------------------
    # Load images
    matchImg = pygame.image.load('assets/images/match3.png')
    quads = GenerateQuads(matchImg.get_width(), matchImg.get_height(), 32, 32)
    print(len(quads))
    print(matchImg.get_width(), matchImg.get_height())
          
    # print(quads)
#---------------------------------------------------------

def init():
    pass

#---------------------------------------------------------

# This function is executed each frame
def update(dt):
    pass

#---------------------------------------------------------

def render(dt):
    global quads

    # Clear the screen with a specific color
    #virtual_screen.fill((0, 0, 0))

    for y in range(0, 288, 32):
        for x in range(0,512,32):
            virtual_screen.blit(matchImg, (x,y), quads[random.randint(0, len(quads)-1)])

    # Scale the virtual screen to the window size
    scale_to_window()

#---------------------------------------------------------

def scale_to_window():
    # Scale the virtual screen surface to the window size
    # If you want to keep the pixelated look:
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # If you want to smooth things out:
    #scaled_surface = pygame.transform.smoothscale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

#---------------------------------------------------------

# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    pass

#---------------------------------------------------------

def main():
    # Load game resources
    load()
    # Initialize game state variables
    init()

    running = True

    # last_time is used to calculate the 'delta time'.
    # Remember: 'delta time' is the time between two consecutive frames
    # get_ticks() returns the number of milliseconds since the program started
    # We divide by 1000 to convert milliseconds to seconds
    last_time = pygame.time.get_ticks() / 1000.0

    while running:
        current_time = pygame.time.get_ticks() / 1000.0  # Current time in seconds
        # Calculate the 'delta time', i.e: the time between two consecutive frames
        dt = current_time - last_time  # Delta time in seconds
        # Update last_time for the next frame
        last_time = current_time
        
        # This is the event loop. It listens for events and executes the appropriate code
        #  depending on the event type. Here we are only interested in keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Space pressed
                if event.key == pygame.K_SPACE:
                    print('Space pressed')
        
        # Continuous key event checking, polling every frame
        handle_input(dt)
        # Update game objects
        update(dt)
        # Draw everything on the screen
        render(dt)
        
        # The flip function is used to copy the contents of the virtual screen
        #   onto the actual window that you see on your monitor.
        pygame.display.flip()
        # Cap the frame rate to 60 frames per second
        clock.tick(FPS)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
