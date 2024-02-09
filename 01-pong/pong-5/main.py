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
import random
from Paddle import Paddle
from Ball import Ball

from config import *

player1 = None
player2 = None
ball = None

game_state = 'start'

# Load resources
def load_game():
    global small_font, score_font, virtual_screen, window, clock, player1, player2, ball
    pygame.init()
    pygame.font.init()  # Initialize font module

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hello Pong!')
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
    small_font = pygame.font.Font('font.ttf', 8)
    score_font = pygame.font.Font('font.ttf', 32)
    clock = pygame.time.Clock()

    player1 = Paddle(10, 30, 5, 20)
    player2 = Paddle(VIRTUAL_WIDTH - 15, VIRTUAL_HEIGHT - 50, 5, 20)
    ball = Ball(VIRTUAL_WIDTH / 2 - 2, VIRTUAL_HEIGHT / 2 - 2, 4, 4)

# Initialize game state
def init_game():
    global game_state, player1, player2, ball

    # Global game state variables
    game_state = 'start'
    player1.score = 0
    player2.score = 0
    ball.reset()
    

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
    
        
def update(dt):
    global game_state, player1, player2, ball
    player1.update(dt)
    player2.update(dt)
    if game_state == 'play':
        ball.update(dt)

def render(dt):
    global player1, player2, game_state, ball
    virtual_screen.fill((40, 45, 52))  # Clear screen with background color
    draw_text('Hello '+ game_state +' State!', small_font, VIRTUAL_WIDTH / 2, 20)
    player1.render(virtual_screen)
    player2.render(virtual_screen)
    ball.render(virtual_screen)
    scale_to_window()

def draw_text(text, font, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    virtual_screen.blit(text_surface, text_rect)

def scale_to_window():
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

def main():
    load_game()
    init_game()
    global game_state, ball
    running = True
    last_time = pygame.time.get_ticks() / 1000.0  # Convert milliseconds to seconds

    while running:
        current_time = pygame.time.get_ticks() / 1000.0  # Current time in seconds
        dt = current_time - last_time  # Delta time in seconds
        last_time = current_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # One time press keys in the event loop
            #    Discrete key event checking, only checks when key is pressed, not every frame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if game_state == 'start':
                        game_state = 'play'
                    else:
                        game_state = 'start'
                        ball.reset()

        handle_input(dt)
        update(dt)
        render(dt)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
