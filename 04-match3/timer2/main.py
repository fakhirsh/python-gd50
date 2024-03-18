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
from TimerManager import TimerManager

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
pygame.display.set_caption('Timer 2')

# Create a surface for the virtual resolution
virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

# The Clock object is responsible for keeping track of time and 
# regulating the frame rate. It provides methods like tick() to 
# control the frame rate and measure the time between frames.
clock = pygame.time.Clock()

# Initialize counters
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

# Example usage
def timer1_action():
    global counter1
    counter1 += 1

def timer2_action():
    global counter2
    counter2 += 1

def timer3_action():
    global counter3
    counter3 += 1

def timer4_action():
    global counter4
    counter4 += 1

def timer5_action():
    global counter5
    counter5 += 1


# Add timers
TimerManager.add_timer(1.0, timer1_action, repeat=3)
TimerManager.add_timer(2.0, timer2_action, repeat=-1)
TimerManager.add_timer(3.0, timer3_action, repeat=5)
TimerManager.add_timer(4.0, timer4_action, repeat=2)
TimerManager.add_timer(5.0, timer5_action, repeat=-1)


#---------------------------------------------------------
    
# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass
    
#---------------------------------------------------------
               
def update(dt):
    TimerManager.update(dt)

#---------------------------------------------------------
        
def render(dt):
    global counter1, counter2, counter3, counter4, counter5

    # Clear the screen with a background color
    virtual_screen.fill((40, 45, 52))
    
    # Render text to the virtual screen
    font = pygame.font.Font(None, 24)  # Adjust font size as needed
    
    text1 = font.render(f'Timer: {counter1} times (every 1 sec)', True, (255, 255, 255))
    text_rect = text1.get_rect(center=(VIRTUAL_WIDTH / 2, 68))  
    virtual_screen.blit(text1, text_rect)

    text2 = font.render(f'Timer: {counter2} times (every 2 sec)', True, (255, 255, 255))
    text_rect = text2.get_rect(center=(VIRTUAL_WIDTH / 2, 68 + 24))
    virtual_screen.blit(text2, text_rect)

    text3 = font.render(f'Timer: {counter3} times (every 3 sec)', True, (255, 255, 255))
    text_rect = text3.get_rect(center=(VIRTUAL_WIDTH / 2, 68 + 24 * 2))
    virtual_screen.blit(text3, text_rect)

    text4 = font.render(f'Timer: {counter4} times (every 4 sec)', True, (255, 255, 255))
    text_rect = text4.get_rect(center=(VIRTUAL_WIDTH / 2, 68 + 24 * 3))
    virtual_screen.blit(text4, text_rect)

    text5 = font.render(f'Timer: {counter5} times (every 5 sec)', True, (255, 255, 255))
    text_rect = text5.get_rect(center=(VIRTUAL_WIDTH / 2, 68 + 24 * 4))
    virtual_screen.blit(text5, text_rect)

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
