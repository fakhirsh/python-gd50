import pygame
import sys
import random

# Actual window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# speed at which we will move our paddle; units per second
PADDLE_SPEED = 200
BALL_SPEED = 60

# Desired framerate
FPS = 60

# Global game state variables
player1_score = 0
player2_score = 0
player1_y = 30
player2_y = VIRTUAL_HEIGHT - 50

ball_x = VIRTUAL_WIDTH / 2 - 2
ball_y = VIRTUAL_HEIGHT / 2 - 2
ball_dx = 0
ball_dy = 0


game_state = 'start'

# Load resources
def load_game():
    pygame.init()
    pygame.font.init()  # Initialize font module

# Initialize game state
def init_game():
    global small_font, score_font, virtual_screen, window, clock, ball_dx, ball_dy, game_state, player1_score, player2_score, player1_y, player2_y, ball_x, ball_y

    # Global game state variables
    game_state = 'start'
    player1_score = 0
    player2_score = 0
    player1_y = 30
    player2_y = VIRTUAL_HEIGHT - 50

    ball_x = VIRTUAL_WIDTH / 2 - 2
    ball_y = VIRTUAL_HEIGHT / 2 - 2
    ball_dx = 100 if random.randint(1, 2) == 1 else -100
    ball_dy = random.randint(-50, 50)

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hello Pong!')
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
    small_font = pygame.font.Font('font.ttf', 8)
    score_font = pygame.font.Font('font.ttf', 32)
    clock = pygame.time.Clock()

# Keep this function for continuous keys. Move one time key presses to main event loop
#  Continuous key event checking, polling every frame
def handle_input(dt):
    global game_state, player1_y, player2_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= PADDLE_SPEED * dt
    if keys[pygame.K_s]:
        player1_y += PADDLE_SPEED * dt
    if keys[pygame.K_UP]:
        player2_y -= PADDLE_SPEED * dt
    if keys[pygame.K_DOWN]:
        player2_y += PADDLE_SPEED * dt
    
        
def update(dt):
    global ball_x, ball_y, ball_dx, ball_dy
    if game_state == 'play':
        ball_x = ball_x + ball_dx * dt
        ball_y = ball_y + ball_dy * dt

def render_graphics():
    global player1_y, player2_y, game_state
    virtual_screen.fill((40, 45, 52))  # Clear screen with background color
    draw_text('Hello '+ game_state +' State!', small_font, VIRTUAL_WIDTH / 2, 20)
    #draw_scores(player1_score, player2_score)
    draw_paddles(player1_y, player2_y)
    draw_ball(ball_x, ball_y)
    scale_to_window()

def draw_text(text, font, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    virtual_screen.blit(text_surface, text_rect)

def draw_scores(score1, score2):
    score1_text = score_font.render(str(score1), True, (255, 255, 255))
    score2_text = score_font.render(str(score2), True, (255, 255, 255))
    virtual_screen.blit(score1_text, (VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3))
    virtual_screen.blit(score2_text, (VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3))

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
    global game_state, ball_x, ball_y, ball_dx, ball_dy
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
                        ball_x = VIRTUAL_WIDTH / 2 - 2
                        ball_y = VIRTUAL_HEIGHT / 2 - 2
                        ball_dx = 100 if random.randint(1, 2) == 1 else -100
                        ball_dy = random.randint(-50, 50)

        handle_input(dt)
        update(dt)
        render_graphics()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
