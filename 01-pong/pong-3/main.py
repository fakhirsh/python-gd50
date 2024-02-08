import pygame
import sys

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# speed at which we will move our paddle; multiplied by dt in update
PADDLE_SPEED = 200

# Desired framerate
FPS = 60

# Global game state variables
player1_y = 30
player2_y = VIRTUAL_HEIGHT - 50

# Load resources
def load_game():
    pygame.init()
    pygame.font.init()  # Initialize font module

# Initialize game state
def init_game():
    global small_font, virtual_screen, window, clock
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hello Pong!')
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
    small_font = pygame.font.Font('font.ttf', 8)
    clock = pygame.time.Clock()

def handle_input():
    global player1_y, player2_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= PADDLE_SPEED / FPS
    if keys[pygame.K_s]:
        player1_y += PADDLE_SPEED / FPS
    if keys[pygame.K_UP]:
        player2_y -= PADDLE_SPEED / FPS
    if keys[pygame.K_DOWN]:
        player2_y += PADDLE_SPEED / FPS

def render_graphics(player1_y, player2_y):
    virtual_screen.fill((40, 45, 52))  # Clear screen with background color
    draw_text('Hello Pong!', small_font, VIRTUAL_WIDTH / 2, 20)
    draw_paddles(player1_y, player2_y)
    draw_ball(VIRTUAL_WIDTH / 2 - 2, VIRTUAL_HEIGHT / 2 - 2)
    scale_to_window()

def draw_text(text, font, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    virtual_screen.blit(text_surface, text_rect)

def draw_paddles(player1_y, player2_y):
    pygame.draw.rect(virtual_screen, (255, 255, 255), (10, player1_y, 5, 20))
    pygame.draw.rect(virtual_screen, (255, 255, 255), (VIRTUAL_WIDTH - 15, player2_y, 5, 20))

def draw_ball(x, y):
    pygame.draw.rect(virtual_screen, (255, 255, 255), (x, y, 4, 4))

def scale_to_window():
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

def main():
    load_game()
    init_game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        handle_input()
        render_graphics(player1_y, player2_y)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
