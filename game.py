import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 410

def player(x,y):
    screen.blit(playerImg, (x,y))


while not done: 
    screen.fill((0,0,0))

    playerY -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player(playerX, playerY)
    pygame.display.update()
