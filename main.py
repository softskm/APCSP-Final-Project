import pygame
import sys

pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avatar Maker")

# Create a list to store the avatars
avatar_list = []

# Initialize variables
current_background = 0
current_face = 0
current_hat = 0
current_shirt = 0
current_pants = 0
current_eye_color = 0

background_colors = [(50, 50, 200), (100, 200, 100), (200, 100, 50)]
face_colors = [(255, 230, 200), (200, 180, 150), (150, 100, 50)]
hat_colors = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]
shirt_colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]
pants_colors = [(150, 150, 150), (100, 100, 100), (50, 50, 50)]
eye_colors = [(255, 255, 255), (200, 200, 200), (150, 150, 150)]

# Load a font for displaying instructions
font = pygame.font.Font(None, 24)

def draw_instructions():
    instructions = [
        "Instructions:",
        "Change background: LEFT/RIGHT arrows",
        "Change face: UP/DOWN arrows",
        "Change hat: A/D keys",
        "Change shirt: W/S keys",
        "Change pants: T/G keys",
        "Change eye color: Y/H keys",
        "Save avatar: S key"
    ]

    y = 10
    for line in instructions:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, y)
        screen.blit(text_surface, text_rect)
        y += 30

def draw_avatar():
    background_color = background_colors[current_background]
    face_color = face_colors[current_face]
    hat_color = hat_colors[current_hat]
    shirt_color = shirt_colors[current_shirt]
    pants_color = pants_colors[current_pants]
    eye_color = eye_colors[current_eye_color]

    # Draw the background
    screen.fill(background_color)

    # Draw the face
    face_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 100, 200, 200)
    pygame.draw.ellipse(screen, face_color, face_rect)

    # Draw the hat
    hat_rect = pygame.Rect(screen_width // 2 - 120, screen_height // 2 - 170, 240, 100)
    pygame.draw.rect(screen, hat_color, hat_rect)

    # Draw the shirt
    shirt_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 + 40, 150, 150)
    pygame.draw.rect(screen, shirt_color, shirt_rect)
    # Draw the pants
    pants_rect1 = pygame.Rect(screen_width // 2 - 75, screen_height // 2 + 190, 60, 150)
    pants_rect2 = pygame.Rect(screen_width // 2 + 15, screen_height // 2 + 190, 60, 150)
    pygame.draw.rect(screen, pants_color, pants_rect1)
    pygame.draw.rect(screen, pants_color, pants_rect2)

    # Draw the eyes
    left_eye_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 40, 50, 50)
    right_eye_rect = pygame.Rect(screen_width // 2, screen_height // 2 - 40, 50, 50)
    pygame.draw.ellipse(screen, eye_color, left_eye_rect)
    pygame.draw.ellipse(screen, eye_color, right_eye_rect)

    # Draw the pupils
    left_pupil_rect = pygame.Rect(screen_width // 2 - 30, screen_height // 2 - 20, 10, 10)
    right_pupil_rect = pygame.Rect(screen_width // 2 + 20, screen_height // 2 - 20, 10, 10)
    pygame.draw.ellipse(screen, (0, 0, 0), left_pupil_rect)
    pygame.draw.ellipse(screen, (0, 0, 0), right_pupil_rect)

    draw_instructions()

def save_avatar():
    avatar_surface = pygame.Surface((screen_width, screen_height))
    draw_avatar()
    pygame.display.flip()
    avatar_list.append(avatar_surface.copy())

def change_item(item_list, current_index, increment):
    return (current_index + increment) % len(item_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_background = change_item(background_colors, current_background, 1)
            if event.key == pygame.K_LEFT:
                current_background = change_item(background_colors, current_background, -1)
            if event.key == pygame.K_UP:
                current_face = change_item(face_colors, current_face, 1)
            if event.key == pygame.K_DOWN:
                current_face = change_item(face_colors, current_face, -1)
            if event.key == pygame.K_a:
                current_hat = change_item(hat_colors, current_hat, 1)
            if event.key == pygame.K_d:
                current_hat = change_item(hat_colors, current_hat, -1)
            if event.key == pygame.K_w:
                current_shirt = change_item(shirt_colors, current_shirt, 1)
            if event.key == pygame.K_s:
                current_shirt = change_item(shirt_colors, current_shirt, -1)
            if event.key == pygame.K_t:
                current_pants = change_item(pants_colors, current_pants, 1)
            if event.key == pygame.K_g:
                current_pants = change_item(pants_colors, current_pants, -1)
            if event.key == pygame.K_y:
                current_eye_color = change_item(eye_colors, current_eye_color, 1)
            if event.key == pygame.K_h:
                current_eye_color = change_item(eye_colors, current_eye_color, -1)
            if event.key == pygame.K_s:
                save_avatar()

    draw_avatar()
    pygame.display.flip()