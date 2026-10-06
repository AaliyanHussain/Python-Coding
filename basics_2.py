import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("She was just a dream and I was the dreamer")
clock = pygame.time.Clock()
running = True
player_x = 100
player_y = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x -= 10
        if event.key == pygame.K_RIGHT:
            player_x += 10
        if event.key == pygame.K_UP:
            player_y -= 10
        if event.key == pygame.K_DOWN:
            player_y += 10
    if player_x < 0:
        player_x = 0
    elif player_x > 800 - 50:
        player_x = 800 - 50

    if player_y < 0:
        player_y = 0
    elif player_y > 600 - 60:
        player_y = 600 - 60
            
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 60))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()



