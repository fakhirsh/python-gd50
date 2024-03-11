
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

class PlayState(State):

    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)
        
        self.pauseSound = pygame.mixer.Sound('assets/sounds/pause.wav')

        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')

        # Load the texture atlas. Convert alpha is used to make the background transparent
        self.atlas = pygame.image.load('assets/images/breakout.png').convert_alpha()
        # Generate quads for the paddles
        self.paddleQuads = GenerateQuadsPaddles(self.atlas)

        self.paddle = Paddle(self.atlas, self.paddleQuads)

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
                self.pauseSound.play()
                if self.isPaused == False:
                    self.isPaused = True
                else:
                    self.isPaused = False

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        if self.isPaused:
            return

        self.paddle.update(dt)
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        
        background_width, background_height = self.backgroundImg.get_size()

        # Scaling the background image
        # First we calculate the scale factor
        scale_x = VIRTUAL_WIDTH / (background_width - 1)
        scale_y = VIRTUAL_HEIGHT / (background_height - 1)
        # Then we create a new background with the new scaled dimensions
        scaled_background = pygame.transform.scale(self.backgroundImg, (int(background_width * scale_x), int(background_height * scale_y)))

        # Drawing the scaled image at coordinates (0, 0)
        virtual_screen.blit(scaled_background, (0, 0))

        # Draw the paddle
        self.paddle.render(virtual_screen)

        # If the game is paused, draw the word "PAUSED" in the middle of the screen
        if self.isPaused:
            draw_text('PAUSED', self.largeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2-16, (255, 255, 255), virtual_screen)

#--------------------------------------------------------------------------------------------------
