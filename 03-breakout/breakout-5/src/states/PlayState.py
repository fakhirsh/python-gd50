
'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
from .State import State
from lib.utils import *
from src.config import *
from src.Paddle import Paddle
from src.Ball import Ball
from src.LevelMaker import LevelMaker
import random

class PlayState(State):
    def __init__(self, assets):
        self.assets = assets
        self.isPaused = False

    def load(self):

        # initialize the paddle, ball, and bricks
        self.paddle = Paddle(self.assets)
        self.ball = Ball(self.assets, self.paddle)
        self.bricks = LevelMaker.createMap(self.assets)
        
        # give ball random starting velocity
        self.ball.dx = random.randint(-200, 200)
        self.ball.dy = random.randint(-60, -50)

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        self.resume()
    
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        self.isPaused = True
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        self.isPaused = False

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the return key
                pass
            elif event.key == pygame.K_SPACE:
                self.assets['sounds']['pause'].play()
                if self.isPaused == False:
                    self.isPaused = True
                else:
                    self.isPaused = False

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        if self.isPaused:
            return

        self.paddle.update(dt)
        self.ball.update(dt)

        # detect collision across all bricks with the ball
        for brick in self.bricks:

            # only check collision if we're in play
            if brick.inPlay and self.ball.checkCollision(brick):

                # trigger the brick's hit function, which removes it from play
                brick.hit()

                # collision code for bricks
                # we check to see if the opposite side of our velocity is outside of the brick;
                # if it is, we trigger a collision on that side. else we're within the X + width of
                # the brick and should check to see if the top or bottom edge is outside of the brick,
                # colliding on the top or bottom accordingly

                # left edge; only check if we're moving right
                if self.ball.x + 2 < brick.x and self.ball.dx > 0:
                    # flip x velocity and reset position outside of brick
                    self.ball.dx = -self.ball.dx
                    self.ball.x = brick.x - 8

                # right edge; only check if we're moving left
                elif self.ball.x + 6 > brick.x + brick.width and self.ball.dx < 0:
                    # flip x velocity and reset position outside of brick
                    self.ball.dx = -self.ball.dx
                    self.ball.x = brick.x + 32

                # top edge if no X collisions, always check
                elif self.ball.y < brick.y:
                    # flip y velocity and reset position outside of brick
                    self.ball.dy = -self.ball.dy
                    self.ball.y = brick.y - 8

                # bottom edge if no X collisions or top collision, last possibility
                else:
                    # flip y velocity and reset position outside of brick
                    self.ball.dy = -self.ball.dy
                    self.ball.y = brick.y + 16

                # slightly scale the y velocity to speed up the game
                self.ball.dy = self.ball.dy * 1.02

                # only allow colliding with one brick, for corners
                break
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        
        background_width, background_height = self.assets['images']['background'].get_size()

        # Scaling the background image
        # First we calculate the scale factor
        scale_x = VIRTUAL_WIDTH / (background_width - 1)
        scale_y = VIRTUAL_HEIGHT / (background_height - 1)
        # Then we create a new background with the new scaled dimensions
        scaled_background = pygame.transform.scale(self.assets['images']['background'], (int(background_width * scale_x), int(background_height * scale_y)))

        # Drawing the scaled image at coordinates (0, 0)
        virtual_screen.blit(scaled_background, (0, 0))

        # Draw the bricks
        for b in self.bricks:
            b.render(virtual_screen)

        # Draw the paddle
        self.paddle.render(virtual_screen)
        # Draw the ball
        self.ball.render(virtual_screen)

        # If the game is paused, draw the word "PAUSED" in the middle of the screen
        if self.isPaused:
            draw_text('PAUSED', self.assets['fonts']['large'], VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2-16, (255, 255, 255), virtual_screen)

#--------------------------------------------------------------------------------------------------
