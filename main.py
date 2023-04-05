import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Simple Game')

# Set up the clock
clock = pygame.time.Clock()

# Define the player and enemy
player_size = 50
player_pos = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - player_size * 2]
enemy_size = 50
enemy_pos = [random.randint(0, WINDOW_SIZE[0] - enemy_size), 0]
enemy_speed = 10

# Define the score font and initial score
font = pygame.font.Font(None, 30)
score = 0

# Define the function to detect collisions
def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size

    # Move the enemy down the screen
    enemy_pos[1] += enemy_speed

    # Check for collision
    if detect_collision(player_pos, enemy_pos):
        score += 1
        enemy_pos = [random.randint(0, WINDOW_SIZE[0] - enemy_size), 0]

    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(30)

# Quit Pygame
pygame.quit()