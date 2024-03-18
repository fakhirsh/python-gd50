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

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# Initialize Pygame
pygame.init()

# Set up the display window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Timer 3')

# Create a surface for the virtual resolution
virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

# The Clock object is responsible for keeping track of time and 
# regulating the frame rate. It provides methods like tick() to 
# control the frame rate and measure the time between frames.
clock = pygame.time.Clock()

#---------------------------------------------------------

# initialize timers
counter1 = 0
counter2 = 0

# Define custom events for timers
TIMER_EVENT1 = pygame.USEREVENT + 1
TIMER_EVENT2 = pygame.USEREVENT + 2

# Set timers (milliseconds)
pygame.time.set_timer(TIMER_EVENT1, 2000)  # Event every 2 seconds
pygame.time.set_timer(TIMER_EVENT2, 5000)  # Event every 5 seconds

#---------------------------------------------------------
    
# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass
    
#---------------------------------------------------------
               
def update(dt):
    pass

#---------------------------------------------------------
        
def render(dt):
    global counter1, counter2, counter3, counter4, counter5

    # Clear the screen with a background color
    virtual_screen.fill((40, 45, 52))
    
    # Render text to the virtual screen
    font = pygame.font.Font(None, 24)  # Adjust font size as needed
    
    text1 = font.render(f'Timer: {counter1} times (every 2 sec)', True, (255, 255, 255))
    text_rect = text1.get_rect(center=(VIRTUAL_WIDTH / 2, 68))  
    virtual_screen.blit(text1, text_rect)

    text2 = font.render(f'Timer: {counter2} times (every 5 sec)', True, (255, 255, 255))
    text_rect = text2.get_rect(center=(VIRTUAL_WIDTH / 2, 68 + 24))
    virtual_screen.blit(text2, text_rect)    

    # Scale the virtual screen to the window size
    scale_to_window()
  
#---------------------------------------------------------
    
def scale_to_window():
    # Once we've drawn everything on the virtual screen, 
    #   we can scale it to the window size
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Finally, draw the scaled surface to the actual window
    window.blit(scaled_surface, (0, 0))

#---------------------------------------------------------


def main():
    global counter1, counter2

    # Main game loop
    running = True

    last_time = pygame.time.get_ticks() / 1000.0

    while running:
        current_time = pygame.time.get_ticks() / 1000.0  # Current time in seconds
        # Calculate the 'delta time', i.e: the time between two consecutive frames
        dt = current_time - last_time  # Delta time in seconds
        # Update last_time for the next frame
        last_time = current_time

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == TIMER_EVENT1:
                # Timer 1 Event: Do something here...
                counter1 += 1
            elif event.type == TIMER_EVENT2:
                # "Timer 2 Event: Do something else here...
                counter2 += 1


        # Update game objects
        update(dt)
        # Draw everything on the screen
        render(dt)

        # Update the display
        pygame.display.flip()

        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
