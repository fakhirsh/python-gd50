'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

import pygame
import random
from .State import State
from utils import draw_text
from config import *
from Bird import Bird
from PipePair import PipePair

class PlayState(State):

    def load(self):
        # initialize our nice-looking retro text fonts
        self.small_font = pygame.font.Font('assets/fonts/font.ttf', 8)
        self.mediumFont = pygame.font.Font('assets/fonts/flappy.ttf', 14)
        self.flappyFont = pygame.font.Font('assets/fonts/flappy.ttf', 28)
        self.hugeFont   = pygame.font.Font('assets/fonts/flappy.ttf', 56)
        # background image and starting scroll location (X axis)
        self.backgroundImg = pygame.image.load('assets/images/background.png')
        # ground image and starting scroll location (X axis)
        self.groundImg = pygame.image.load('assets/images/ground.png')
        # Create bird object
        self.bird = Bird()

        print("PlayState: load")

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        self.small_font = None
        self.mediumFont = None
        self.flappyFont = None
        self.hugeFont   = None
        print("PlayState: unload")

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        print("PlayState: init")
        # List of Pipe objects
        self.pipesPairs = []
        # Timer for spawning pipes
        self.pipeSpawnTimer = 0
        # initialize our last recorded Y value for a gap placement to base other gaps off of
        self.lastY = VIRTUAL_HEIGHT / 2
        self.gameOver = False
        self.backgroundScroll = 0
        self.groundScroll = 0
        self.pipeSpawnTimer = 0
        self.score = 0
        
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bird.applyForce()

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):

        if self.gameOver:
            from .ScoreState import ScoreState
            self.stateManager.changeState(ScoreState({'score': self.score}))
            return

        # Scroll background by preset speed * dt, looping back to 0 after the looping point
        self.backgroundScroll = (self.backgroundScroll + BACKGROUND_SCROLL_SPEED * dt) % BACKGROUND_LOOPING_POINT
        
        # Scroll ground by preset speed * dt, looping back to 0 after the screen width passes
        self.groundScroll = (self.groundScroll + GROUND_SCROLL_SPEED * dt) % VIRTUAL_WIDTH
    
        # spawn a new Pipe if the timer is past 2 seconds
        if self.pipeSpawnTimer > 2:
            # Modify the last Y coordinate we placed so pipe gaps aren't too far apart
            y = self.lastY + random.randint(-PIPE_Y_VARIATION, PIPE_Y_VARIATION)
            # Check if the y coordinate is below the ground level
            #   no lower than a gap height (90 pixels) from the bottom
            if y > VIRTUAL_HEIGHT - GAP_HEIGHT:
                # If it is, set the y coordinate to the ground level minus a buffer
                # This prevents the pipes from going below the ground
                y = VIRTUAL_HEIGHT - GAP_HEIGHT
            # No higher than 10 pixels below the top edge of the screen,
            elif y < GAP_HEIGHT + 10:
                # If it is, set the y coordinate to the gap height plus a buffer
                # This prevents the pipes from going above the gap
                y = GAP_HEIGHT + 10

            # Set the lastY to the current y coordinate
            lastY = y

            # Add a new pair of pipes at the end of the screen at the specified y
            self.pipesPairs.append(PipePair(y))
            self.pipeSpawnTimer = 0

        # Update bird
        self.bird.update(dt)

        self.pipeSpawnTimer += dt

        # Update all the pipes in the scene
        for pair in self.pipesPairs:
            pair.update(dt)

            # Check for collisions between the bird and all pipes in the scene
            for pipe in pair.pipes.values():
                # If the bird collides with any pipe, stop the game from scrolling
                if self.bird.collides(pipe):
                    self.gameOver = True
                    return
                elif not pair.scored and pipe.x + pipe.width < self.bird.x:
                    self.score = self.score + 1
                    pair.scored = True

            # Remove any flagged pipes
            if pair.remove:
                self.pipesPairs.remove(pair)

        # If the bird collides with the ground, stop the game from scrolling
        if self.bird.y + self.bird.height >= VIRTUAL_HEIGHT - self.groundImg.get_height():
            self.gameOver = True

#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
         # Clear the virtual screen
        #virtual_screen.fill((0, 0, 0))
        
        # Draw the background at the negative looping point
        virtual_screen.blit(self.backgroundImg, (-self.backgroundScroll, 0))

        # Draw all the pipes
        for pair in self.pipesPairs:
            pair.render(virtual_screen)

        # Draw the ground on top of the background, toward the bottom of the screen,
        # at its negative looping point
        virtual_screen.blit(self.groundImg, (-self.groundScroll, VIRTUAL_HEIGHT - self.groundImg.get_height()))

        draw_text(str(self.score), self.flappyFont, 16, 16, (255, 255, 255), virtual_screen)
        
        # Draw the bird
        self.bird.render(virtual_screen)

#--------------------------------------------------------------------------------------------------
