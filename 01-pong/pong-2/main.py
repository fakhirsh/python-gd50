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
pygame.display.set_caption('Pong 2')

# Create a surface for the virtual resolution
virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

def draw_virtual_screen():
    # Fill the screen with somewhat original Pong's color
    virtual_screen.fill((40, 45, 52))
    
    # Load the custom font and render text to the virtual screen
    font_path = "font.ttf"  # Specify the path to your font file here
    font_size = 8  # Adjust font size as needed
    font = pygame.font.Font(font_path, font_size)  # Use the custom font
    text = font.render('Hello Pong!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(VIRTUAL_WIDTH / 2, 20))
    virtual_screen.blit(text, text_rect)

    #-----------------------------------------------------
    white_color = (255, 255, 255)  # White
    paddle_width = 5
    paddle_height = 20
    # left paddle
    pygame.draw.rect(virtual_screen, white_color, (10, 30, paddle_width, paddle_height))
    paddle_x = VIRTUAL_WIDTH - 10
    paddle_y = VIRTUAL_HEIGHT - 50
    # right paddle
    pygame.draw.rect(virtual_screen, white_color, (paddle_x, paddle_y, paddle_width, paddle_height))
    # ball
    pygame.draw.rect(virtual_screen, white_color, (VIRTUAL_WIDTH/2-2, VIRTUAL_HEIGHT/2-2, 4, 4))
    #-----------------------------------------------------
def scale_to_window():
    # Scale the virtual screen surface to the window size
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
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

if __name__ == "__main__":
    main()
