import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake properties
snake_size = 20
snake_speed = 5 

snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2
snake_body = []
snake_length = 1

# Food properties
food_x = round(random.randrange(0, SCREEN_WIDTH - snake_size) / snake_size) * snake_size
food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_size) / snake_size) * snake_size

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Direction
direction = "RIGHT"
change_to = direction

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != "DOWN":
                    change_to = "UP"
            elif event.key == pygame.K_DOWN:
                if direction != "UP":
                    change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                if direction != "RIGHT":
                    change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if direction != "LEFT":
                    change_to = "RIGHT"

    direction = change_to

    if direction == "UP":
        snake_y -= snake_size
    if direction == "DOWN":
        snake_y += snake_size
    if direction == "LEFT":
        snake_x -= snake_size
    if direction == "RIGHT":
        snake_x += snake_size

    # Snake body growing mechanism
    snake_body.append([snake_x, snake_y])
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Snake collision with itself
    for block in snake_body[:-1]:
        if block == [snake_x, snake_y]:
            running = False

    #******************************************STUDENT ACTIVITY**********************************************************************     
    #snake collision with walls
    if snake_x < 0:
        running = False
    elif snake_x>=SCREEN_WIDTH:
        running=False
    elif snake_y < 0:
        running=False
    elif snake_y >= SCREEN_HEIGHT:
        running=False

    # Snake eats food and its length is increase
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, SCREEN_WIDTH - snake_size) / snake_size) * snake_size
        food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_size) / snake_size) * snake_size
        snake_length = snake_length-1

    
    #********************************************************************************************************************************

    # Fill screen with black background
    screen.fill(WHITE)

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])

    # Draw food
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
