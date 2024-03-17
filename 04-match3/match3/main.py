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
from src.Global import Global
from src.StateManager import StateManager
from src.states.LoadState import LoadState
from lib.Utils import *

#---------------------------------------------------------
# Global variables

window = None
clock = None

last_time = 0

#---------------------------------------------------------

def load():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''

    global window, clock

    # Initialize pygame
    pygame.init()

    # Create game window of size WINDOW_WIDTH x WINDOW_HEIGHT
    window = pygame.display.set_mode((Global.WINDOW_WIDTH, Global.WINDOW_HEIGHT))
    
    # Set window title
    pygame.display.set_caption('Match-3')
    
    # Create a virtual screen to draw on before scaling to the window size
    #  Basically we want to draw everything on a smaller screen and then 
    #  scale it up to the window size
    Global.virtual_screen = pygame.Surface((Global.VIRTUAL_WIDTH, Global.VIRTUAL_HEIGHT))

    # The Clock object is responsible for keeping track of time and 
    # regulating the frame rate. It provides methods like tick() to 
    # control the frame rate and measure the time between frames.
    clock = pygame.time.Clock()

    # Initialize the StateManager.
    # The StateManager is responsible for managing different game states.
    #   It keeps track of the current state and calls the appropriate methods
    #   (load, init, update, render, etc.) for the current state.
    Global.stateManager = StateManager()

    Global.assets['fonts'] = {}
    # Load small font for FPS
    Global.assets['fonts']['small'] = pygame.font.Font('assets/fonts/font.ttf', 8)
    # Load Large font for the loading screen
    Global.assets['fonts']['large'] = pygame.font.Font('assets/fonts/font.ttf', 32)

    Global.assets['sounds'] = {}
    # Load the game music
    Global.assets['sounds']['music'] = pygame.mixer.music.load('assets/sounds/music3.mp3')

#---------------------------------------------------------

def init():
    '''
    This function initializes the game state variables.
    Note that everything was loaded earlier in the load() function.
    '''
        
    # Change the current state to StartState
    Global.stateManager.changeState(LoadState())

#---------------------------------------------------------

def render(dt):

    # Draw the current state
    Global.stateManager.render(dt)
    # Scale the virtual screen to the window size

    # Display the FPS on the virtual screen
    display_fps(int(clock.get_fps()))

    scale_to_window()
    
#---------------------------------------------------------

def scale_to_window():
    # Scale the virtual screen surface to the window size
    # If you want to keep the pixelated look:
    scaled_surface = pygame.transform.scale(Global.virtual_screen, (Global.WINDOW_WIDTH, Global.WINDOW_HEIGHT))
    # If you want to smooth things out:
    #scaled_surface = pygame.transform.smoothscale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

#---------------------------------------------------------

# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    pass

#---------------------------------------------------------

# This function is executed each frame
def update(dt):
    Global.stateManager.update(dt)

#---------------------------------------------------------

def main():
    global last_time

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
                print("QUIT event")
                running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #print("ESCAPE key pressed")
                        running = False
                        return
                # Pass the event to the current active game state
                Global.stateManager.handle_event(event)
        
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
        clock.tick(Global.FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
