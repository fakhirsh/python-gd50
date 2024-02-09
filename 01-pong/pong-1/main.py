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
pygame.display.set_caption('Pong 1')

# Create a surface for the virtual resolution
virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

def draw_virtual_screen():
    # Fill the screen with somewhat original Pong's color
    virtual_screen.fill((40, 45, 52))
    
    # Render text to the virtual screen
    font = pygame.font.Font(None, 24)  # Adjust font size as needed
    text = font.render('Hello Pong!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT / 2))
    virtual_screen.blit(text, text_rect)

def scale_to_window():
    # Scale the virtual screen surface to the window size
    # If you want to keep the pixelated look:
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # If you want to smooth things out:
    #scaled_surface = pygame.transform.smoothscale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

def main():
    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        draw_virtual_screen()
        scale_to_window()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()