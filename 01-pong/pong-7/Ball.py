import random
import pygame
from config import *
import random

class Ball:
    COLOR = (255, 255, 255)
    def __init__(self, x, y, width, height, paddle1, paddle2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = -100 if random.randint(1, 2) == 1 else 100
        self.dx = random.randint(-100, -80) if random.randint(1, 2) == 1 else random.randint(80, 100)
        #--------------------
        self.paddle1 = paddle1
        self.paddle2 = paddle2

    def reset(self):
        self.x = VIRTUAL_WIDTH // 2
        self.y = VIRTUAL_HEIGHT // 2
        self.dy = -100 if random.randint(1, 2) == 1 else 100
        self.dx = random.randint(-100, -80) if random.randint(1, 2) == 1 else random.randint(80, 100)

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        # check collision with screen boundries
        if self.y <= 0:
            self.y = 0
            self.dy = -self.dy
        elif self.y >= VIRTUAL_HEIGHT - self.height:
            self.y = VIRTUAL_HEIGHT - self.height
            self.dy = -self.dy

        # check collision with paddles
        if self.checkCollision(self.paddle1):
            self.x = self.paddle1.x + self.paddle1.width
            self.dx = -self.dx * 1.03
            self.dy += self.paddle1.dy / 4
        elif self.checkCollision(self.paddle2):
            self.x = self.paddle2.x - self.width
            self.dx = -self.dx * 1.03
            self.dy += self.paddle2.dy / 4
            

    def checkCollision(self, rect):
        if self.x > rect.x + rect.width or self.x + self.width < rect.x:
            return False
        if self.y > rect.y + rect.height or self.y + self.height < rect.y:
            return False
        return True
        

        # if self.x < paddle.x + paddle.width and self.x + self.width > paddle.x and self.y < paddle.y + paddle.height and self.y + self.height > paddle.y:
        #     self.dx = -self.dx
        #     self.x = paddle.x + paddle.width if self.dx > 0 else paddle.x - self.width
        #     self.dy += paddle.dy / 4
        #     return True
        # return False


    def render(self, screen):
        pygame.draw.rect(screen, Ball.COLOR, (self.x, self.y, self.width, self.height))

    