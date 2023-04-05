import pygame

# initialize pygame
pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255)

# define window size
WINDOW_SIZE = (400, 400)

# create window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Avatar Maker")

# define avatar options
hair_options = [BLACK, RED, GREEN, BLUE]
skin_options = [WHITE, (255, 224, 189), (220, 133, 83), (139, 69, 19)]
eye_options = [BLUE, (139, 0, 0), (34, 139, 34), (255, 215, 0)]

# define selected options
selected_hair = 0
selected_skin = 0
selected_eye = 0

# define hair
hair_rect = pygame.Rect(100, 100, 200, 50)
hair_surface = pygame.Surface((200, 50))

# define face
face_rect = pygame.Rect(125, 150, 150, 200)
face_surface = pygame.Surface((150, 200))
face_surface.fill(WHITE)

# define eyes
eye1_rect = pygame.Rect(150, 200, 50, 50)
eye2_rect = pygame.Rect(200, 200, 50, 50)
eye1_surface = pygame.Surface((50, 50))
eye2_surface = pygame.Surface((50, 50))

# main game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # check if hair was clicked
            if hair_rect.collidepoint(pos):
                selected_hair += 1
                if selected_hair == len(hair_options):
                    selected_hair = 0
            # check if skin was clicked
            elif face_rect.collidepoint(pos):
                selected_skin += 1
                if selected_skin == len(skin_options):
                    selected_skin = 0
            # check if eyes were clicked
            elif eye1_rect.collidepoint(pos) or eye2_rect.collidepoint(pos):
                selected_eye += 1
                if selected_eye == len(eye_options):
                    selected_eye = 0
                    
    # update hair
    hair_surface.fill(hair_options[selected_hair])
    
    # update eyes
    eye1_surface.fill(eye_options[selected_eye])
    eye2_surface.fill(eye_options[selected_eye])
    
    # draw avatar
    screen.fill(WHITE)
    pygame.draw.rect(screen, hair_options[selected_hair], hair_rect)
    pygame.draw.rect(screen, skin_options[selected_skin], face_rect)
    screen.blit(eye1_surface, eye1_rect)
    screen.blit(eye2_surface, eye2_rect)
    
    # update display
    pygame.display.update()

# quit pygame
pygame.quit()