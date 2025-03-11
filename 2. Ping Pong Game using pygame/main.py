import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15

# Paddle positions
player1_x, player1_y = 20, HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x, player2_y = WIDTH - 35, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position and speed
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4 * random.choice((1, -1)), 4 * random.choice((1, -1))

# Paddle speeds
player_speed = 5
ai_speed = 4

# Game mode: True = AI, False = Player
play_with_ai = False  # Change this to False for two-player mode

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= player_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += player_speed
    
    # Player 2 controls or AI
    if play_with_ai:
        if ball_y > player2_y + PADDLE_HEIGHT // 2 and player2_y < HEIGHT - PADDLE_HEIGHT:
            player2_y += ai_speed
        elif ball_y < player2_y + PADDLE_HEIGHT // 2 and player2_y > 0:
            player2_y -= ai_speed
    else:
        if keys[pygame.K_UP] and player2_y > 0:
            player2_y -= player_speed
        if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
            player2_y += player_speed
    
    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if (ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT) or \
       (ball_x >= player2_x - BALL_SIZE and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT):
        ball_speed_x *= -1
    
    # Ball reset on scoring
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x, ball_speed_y = 4 * random.choice((1, -1)), 4 * random.choice((1, -1))
    
    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()