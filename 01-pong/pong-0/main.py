import pygame
import sys

def main():
    # Constants for the window dimensions
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pong 0')

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with somewhat original Pong's color
        screen.fill((40, 45, 52))

        # Set up the font and render the text
        font = pygame.font.Font(None, 18)  # None uses the default font, 36 is the font size
        text = font.render('Hello Pong!', True, (255, 255, 255))  # White color
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        # Blit the text onto the screen
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()