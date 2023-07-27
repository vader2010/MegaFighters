import pygame

pygame.init()

# create a game window

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("smash_cave")

# load background image

bg_image = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\assets\\selection\\maps\\cave.png").convert_alpha()

# function for drawing background

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    
# game loop

run = True
while run:

    # draw background

    draw_bg()

   # event handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display

    pygame.display.update()
    
# exit pygame

pygame.quit()
