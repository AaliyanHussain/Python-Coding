import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("She was just a dream and I was the dreamer")
clock = pygame.time.Clock()
running = True
player_x = 100
player_y = 200
david = pygame.image.load("player.png").convert_alpha()
david = pygame.transform.scale(david, (16, 16))
while running:
    print(f"x: {player_x}, y: {player_y}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5   
    if player_x < 0:
        print("Hit Left Wall!")
        player_x = 0
    if player_x > 800 - 16:
        print("Hit Right Wall!")
        player_x = 800 - 16

    if player_y < 0:
        player_y = 0
    if player_y > 600 - 16:

        player_y = 600 - 16
            
    screen.fill((50, 50, 50))
    screen.blit(david, (player_x, player_y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()