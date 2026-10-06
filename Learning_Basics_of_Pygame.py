import pygame
import sys
pygame.init()
Screen_Width = 800
Screen_Height = 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("David's Nightmare")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0,))
    pygame.draw.rect(screen, (255, 255, 255), (100, 200 ,50 ,80))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

            