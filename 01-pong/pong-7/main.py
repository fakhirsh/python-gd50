
import pygame
import sys
from Paddle import Paddle
from Ball import Ball

#  Import constant variables from config.py
from config import *

#---------------------------------------------------------
# Global game state variables
player1 = None
player2 = None
ball = None
game_state = 'start'
#---------------------------------------------------------

def load_game():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''
    global small_font, score_font, virtual_screen, window, clock, player1, player2, ball
    
    # Initialize pygame
    pygame.init()
    # Initialize font module
    pygame.font.init()
    
    # Create game window of size WINDOW_WIDTH x WINDOW_HEIGHT
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Set window title
    pygame.display.set_caption('Hello Pong!')
    
    # Create a virtual screen to draw on before scaling to the window size
    #  Basically we want to draw everything on a smaller screen and then 
    #  scale it up to the window size
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
    
    # Load fonts
    small_font = pygame.font.Font('font.ttf', 8)
    score_font = pygame.font.Font('font.ttf', 32)

    # The Clock object is responsible for keeping track of time and 
    # regulating the frame rate. It provides methods like tick() to 
    # control the frame rate and measure the time between frames.
    clock = pygame.time.Clock()

    # Create game objects
    player1 = Paddle(10, 30, 5, 20)
    player2 = Paddle(VIRTUAL_WIDTH - 15, VIRTUAL_HEIGHT - 50, 5, 20)
    
    # Start the ball in the middle of the screen. Also the ball object 
    #   needs to know about the paddles so that it can check for collision
    ball = Ball(VIRTUAL_WIDTH / 2 - 2, VIRTUAL_HEIGHT / 2 - 2, 4, 4, player1, player2)

#---------------------------------------------------------
    
def init_game():
    '''
    This function initializes the game state variables.
    Note that everything was loaded earlier in the load_game() function.
    '''
    global game_state, player1, player2, ball

    # Global game state variable
    game_state = 'start'

    # Initialize player scores
    player1.score = 0
    player2.score = 0
    
    # Reset the ball
    ball.reset()

#---------------------------------------------------------
    
# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    global game_state, player1, player2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.moveUp()
    if keys[pygame.K_s]:
        player1.moveDown()
    if keys[pygame.K_UP]:
        player2.moveUp()
    if keys[pygame.K_DOWN]:
        player2.moveDown()
    
 #---------------------------------------------------------
               
def update(dt):
    global game_state, player1, player2, ball
    
    # Update game objects
    player1.update(dt)
    player2.update(dt)

    # Update ball only if game state is 'play'
    if game_state == 'play':
        ball.update(dt)
        
def render(dt):
    global player1, player2, game_state, ball
    
    # Clear the screen with a background color
    virtual_screen.fill((40, 45, 52))
    
    # Draw Text
    draw_text('Hello '+ game_state +' State!', small_font, VIRTUAL_WIDTH / 2, 20)
    draw_scores(player1.score, player2.score)

    # Draw game objects
    player1.render(virtual_screen)    
    player2.render(virtual_screen)
    ball.render(virtual_screen)
    
    # Display FPS
    display_fps()

    # Scale the virtual screen to the window size
    scale_to_window()

#---------------------------------------------------------
    
def draw_text(text, font, x, y):
    '''
    In PyGame, text is drawn in two steps:
      1. Render the text on a temporary surface
      2. Draw the text surface on the screen buffer
    '''
    # Render the text on a temporary surface
    text_surface = font.render(text, True, (255, 255, 255))
    
    # Get the rectangle of the text surface. Also, 
    #   Center the text at (x, y).
    #   If we don't center the text, then the default position 
    #     is at the top left corner of the text surface
    text_rect = text_surface.get_rect(center=(x, y))
    
    # Finally draw the text surface on the virtual screen buffer
    virtual_screen.blit(text_surface, text_rect)
   
def draw_scores(score1, score2):
    # Render the scores on a temporary surfaces
    # The render function takes the following parameters:
    #   - The text to render
    #   - Anti-aliasing: True or False
    #   - The color of the text
    score1_text = score_font.render(str(score1), True, (255, 255, 255))
    score2_text = score_font.render(str(score2), True, (255, 255, 255))
    
    # Here we didn't center the text, so the default position is 
    #   at the top left corner of the text surface
    virtual_screen.blit(score1_text, (VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3))
    virtual_screen.blit(score2_text, (VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3))

def display_fps():
    # simple FPS display across all states
    # The render function takes the following parameters:
    #   - The text to render
    #   - Anti-aliasing: True or False
    #   - The color of the text
    fps_text = small_font.render('FPS: ' + str(int(clock.get_fps())), True, (0, 255, 0))
    
    # Finally draw the text surface on the virtual screen buffer
    virtual_screen.blit(fps_text, (10, 10))

#---------------------------------------------------------
    
def scale_to_window():
    # Once we've drawn everything on the virtual screen, 
    #   we can scale it to the window size
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Finally, draw the scaled surface to the actual window
    window.blit(scaled_surface, (0, 0))

#---------------------------------------------------------

def main():
    # Load game resources
    load_game()
    # Initialize game state variables
    init_game()

    global game_state, ball

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
            # One time press keys in the event loop
            #    Discrete key event checking, only checks when key is pressed, not every frame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Toggle game state between 'start' and 'play' on space bar press
                if event.key == pygame.K_SPACE:
                    if game_state == 'start':
                        game_state = 'play'
                    else:
                        game_state = 'start'
                        ball.reset()

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
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
