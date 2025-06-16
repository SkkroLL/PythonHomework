import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.circle(screen, BLUE, (200, 150), 50)   
    pygame.draw.circle(screen, YELLOW, (600, 150), 75) 

    pygame.draw.line(screen, RED, (200, 150), (600, 400), 4)  
    pygame.draw.line(screen, PURPLE, (500, 450), (600, 400), 6)

    rect1 = pygame.Rect(100, 450, 80, 80)
    rect2 = pygame.Rect(600, 450, 120, 120)
    pygame.draw.rect(screen, GREEN, rect1)
    pygame.draw.rect(screen, WHITE, rect2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()