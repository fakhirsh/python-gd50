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
         # This is the event loop. It listens for events and executes the appropriate code
        #  depending on the event type.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with somewhat original Pong's color
        screen.fill((40, 45, 52))

        # Set up the font and render the text
        # - First parameter means the font type. 
        #   None means default system font
        # - Second parameter is the font size
        font = pygame.font.Font(None, 18)  # Adjust font size as needed
        
        # In PyGame, text is drawn in two steps:
        #   1. Render the text on a temporary surface
        #   2. Draw the text surface on the screen buffer
        
        # Here, first render the text on a temporary surface
        #   using white color
        text = font.render('Hello Pong!', True, (255, 255, 255))

        # Get the rectangle of the text surface. Also, 
        #   Center the text at (x, y).
        #   If we don't center the text, then the default position 
        #     is at the top left corner of the text surface
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        # Finally draw the text surface on the screen buffer
        #  'blit' means to 'draw'
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