# Snake Game in Python using Pygame

# Import modules
import pygame
import time
import random

# Define constants
snake_speed = 10
window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Define snake position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction

# Define score
score = 0

# Define font
font = pygame.font.SysFont('times new roman', 35)

# Define function to display score
def show_score(choice, color, font, size):
    score_surface = font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x/10, 15)
    else:
        score_rect.midtop = (window_x/2, window_y/1.25)
    game_window.blit(score_surface, score_rect)

# Define function to display game over message
def game_over():
    game_over_surface = font.render('Game Over :(', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, font, 35)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Main loop
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Change direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Grow snake
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Spawn fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # Fill background
    game_window.fill(black)

    # Draw snake and fruit
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Check for collisions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Show score
    show_score(1, white, font, 20)

    # Update display
    pygame.display.update()
    

    # Control frame rate
    fps.tick(snake_speed)
