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
from config import *
from Bird import Bird
from Pipe import Pipe

#---------------------------------------------------------
# Global game state variables

# background image and starting scroll location (X axis)
backgroundImg = None
backgroundScroll = 0

# ground image and starting scroll location (X axis)
groundImg = None
groundScroll = 0

virtual_screen = None
window = None
clock = None

# Bird object
bird = None

# List of Pipe objects
pipes = []
# Timer for spawning pipes
pipeSpawnTimer = 0

#---------------------------------------------------------

def load():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''

    global window, virtual_screen, clock, backgroundImg, groundImg, bird

    # Initialize pygame
    pygame.init()

    # Create game window of size WINDOW_WIDTH x WINDOW_HEIGHT
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Set window title
    pygame.display.set_caption('FC Bird')
    
    # Create a virtual screen to draw on before scaling to the window size
    #  Basically we want to draw everything on a smaller screen and then 
    #  scale it up to the window size
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

    # The Clock object is responsible for keeping track of time and 
    # regulating the frame rate. It provides methods like tick() to 
    # control the frame rate and measure the time between frames.
    clock = pygame.time.Clock()

    # Load images
    backgroundImg = pygame.image.load('assets/images/background.png')
    groundImg = pygame.image.load('assets/images/ground.png')

    # Create bird object
    bird = Bird()

#---------------------------------------------------------

def init():
    '''
    This function initializes the game state variables.
    Note that everything was loaded earlier in the load() function.
    '''

    global backgroundScroll, groundScroll

    backgroundScroll = 0
    groundScroll = 0

#---------------------------------------------------------

def render(dt):
    # Here, we draw our images shifted to the left by their looping point; eventually,
    # they will revert back to 0 once a certain distance has elapsed, which will make it
    # seem as if they are infinitely scrolling. choosing a looping point that is seamless
    # is key, so as to provide the illusion of looping

    global backgroundScroll, groundScroll

    # Clear the virtual screen
    virtual_screen.fill((0, 0, 0))

    # Draw the background at the negative looping point
    virtual_screen.blit(backgroundImg, (-backgroundScroll, 0))

    # Draw the ground on top of the background, toward the bottom of the screen,
    # at its negative looping point
    virtual_screen.blit(groundImg, (-groundScroll, VIRTUAL_HEIGHT - groundImg.get_height()))

    # Draw the bird
    bird.render(virtual_screen)

    for pipe in pipes:
        pipe.render(virtual_screen)

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

# This function is executed each frame
def update(dt):
    global backgroundScroll, groundScroll, pipeSpawnTimer

    # Scroll background by preset speed * dt, looping back to 0 after the looping point
    backgroundScroll = (backgroundScroll + BACKGROUND_SCROLL_SPEED * dt) % BACKGROUND_LOOPING_POINT
    
    # Scroll ground by preset speed * dt, looping back to 0 after the screen width passes
    groundScroll = (groundScroll + GROUND_SCROLL_SPEED * dt) % VIRTUAL_WIDTH

    # Update bird
    bird.update(dt)

    # Update pipes
    for pipe in pipes:
        pipe.update(dt)


    pipeSpawnTimer += dt

    # spawn a new Pipe if the timer is past 2 seconds
    if pipeSpawnTimer > 2:
        pipes.append(Pipe())
        print('Added new pipe!')
        pipeSpawnTimer = 0
      
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
                    # Apply a force to the bird. Bird will jump up and then fall down due to gravity
                    bird.applyForce()
        
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
