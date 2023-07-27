import pygame
class Soldier():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

    def move(self, screen_width, screen_height):
        SPEED = 5
        GRAVITY = 1
        dx = 0
        dy = 0

        # Get keypresses

        key = pygame.key.get_pressed()

        # Movement

        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        # Jump
        
        if key[pygame.K_w]:
            self.vel_y = -30

        # Apply gravity

        self.vel_y += GRAVITY
        dy += self.vel_y 

        # Ensure player stays on screen

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            dy = screen_height - 110 - self.rect.bottom

        # Update player position

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
