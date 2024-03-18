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
import math
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
birdImg = None
MOVE_DURATION = 5
birds = []

end_x, end_y = 0,0

# tweening variable
timer = 0
# longest possible movement duration
TIMER_MAX = 10
#---------------------------------------------------------

def linear(start_val, end_val, t, duration):
    if duration <= 0:
        raise ValueError("duration must be greater than 0")
    # Clamp t to be within the range [0, DURATION]
    t = max(0, min(t, duration))
    return start_val + (end_val - start_val) * t / duration

def ease_in_quad(start_val, end_val, t, duration):
    t = max(0, min(t, duration)) / duration  # Normalize t to [0, 1]
    return start_val + (end_val - start_val) * (t**2)

def ease_out_quad(start_val, end_val, t, duration):
    t = max(0, min(t, duration)) / duration  # Normalize t to [0, 1]
    return start_val - (end_val - start_val) * (t * (t - 2))

def easeOutElastic(start_val, end_val, t, duration):
    if t == 0:
        return start_val
    t /= duration
    if t == 1:
        return end_val
    # Adjusting the period to control the frequency of bounces
    p = duration * 0.3  # This period might result in around 3-4 bounces
    # Adjusted amplitude to a fixed proportion of the movement range
    a = (end_val - start_val) * 0.25
    s = p / 4
    return a * math.pow(2, -10 * t) * math.sin((t * duration - s) * (2 * math.pi) / p) + end_val


#---------------------------------------------------------

def load():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''

    global window, virtual_screen, clock, birdImg, birds

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
    birdImg = pygame.image.load('assets/images/bird.png')

    # table of birds with random movement rates and Y positions
    birds = []

    # create 1000 random birds
    for i in range(1000):
        birds.append({
            # all start at left side
            'x': 0,

            # random Y position within screen boundaries
            'y': random.randint(0, VIRTUAL_HEIGHT - 24),

            # random rate between half a second and our max, floating point
            # random.random() by itself will generate a random float between 0 and 1,
            # so we add that to random.randint(max) to get a number between 0 and 10,
            # floating-point
            'rate': random.random() + random.randint(0, TIMER_MAX - 1),
        })

#---------------------------------------------------------

def init():
    global bird_x, bird_y, end_x, end_y, timer
    '''
    This function initializes the game state variables.
    Note that everything was loaded earlier in the load() function.
    '''
    bird_y = VIRTUAL_HEIGHT / 2 - birdImg.get_height() / 2

    end_x = VIRTUAL_WIDTH - birdImg.get_width()
    end_y = bird_y

    #---------------------------------------------------------
    
    # tweening variable
    timer = 0

#---------------------------------------------------------

# This function is executed each frame
def update(dt):
    global birds, timer, end_x

    # Increment timer by dt
    timer += dt

    # iterating over all birds this time, calculating based on their own rate
    for bird in birds:
        # math.min ensures we don't go past the end
        # timer / MOVE_DURATION is a ratio that we effectively just multiply our
        # X by each turn to make it seem as if we're moving right
        bird['x'] = linear(0, end_x, timer, bird['rate'])


#---------------------------------------------------------

def render(dt):
    global birds, birdImg

    # Clear the screen with a specific color
    virtual_screen.fill((0, 0, 0))

    #virtual_screen.blit(birdImg, (bird_x, bird_y))

    for bird in birds:
        virtual_screen.blit(birdImg, (bird['x'], bird['y']))

    font = pygame.font.Font(None, 16)
    text = font.render(f'{int(clock.get_fps())}', True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(4, 4))
    virtual_screen.blit(text, text_rect)

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
