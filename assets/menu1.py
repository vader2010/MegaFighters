import pygame

pygame.init()

# create a game window

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("menu")

# load background image

bg_image = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\background.png").convert_alpha()

# load buttons

start = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\start.png").convert_alpha()
volume = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\volume.png").convert_alpha()
quits = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\quits.png").convert_alpha()
yes = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\yes_button.png").convert_alpha()
no = pygame.image.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\no_button.png").convert_alpha()

# function for drawing background

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    
# button class

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def buttons(self):
        
        action = False

        # get mouse position

        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
# create buttons

start_button = Button(475, 200, start, 4)
volume_button = Button(400, 350, volume, 4)
quit_button = Button(475, 275, quits, 4)
yes_button = Button(700, 350, yes, 2)
no_button = Button(800, 350, no, 2)

# game loop

run = True
while run:

    # draw background

    draw_bg()

    # add music

    if yes_button.buttons():

        pygame.mixer.music.load("C:\\Users\\Abhinab\\.vscode\\MegaFighters\\Assets\\menu\\music.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        
    if no_button.buttons():
        pygame.mixer.music.stop()

    # draw buttons

    if start_button.buttons():
        import selection_map

    volume_button.buttons()

    if quit_button.buttons():
        run = False

    # event handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display

    pygame.display.update()
    
# exit pygame

pygame.quit()