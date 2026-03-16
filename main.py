import pygame
import random

HEIGHT, WIDTH = 800, 800
x, y = 0, 0
radius = 1

running = True
active = False

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            active = True
            radius = 1
            color = random_color()
            x, y = pygame.mouse.get_pos()
            
    screen.fill((0, 0, 0))
    
    if active:
        pygame.draw.circle(screen, color, (x, y), radius)
        radius += 4
        
    if radius > 100: 
        active = False
        x, y = 0, 0
        radius = 1
            
    pygame.display.flip()
    clock.tick(60)