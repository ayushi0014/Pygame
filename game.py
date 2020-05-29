import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False

#background
background = pygame.image.load('background.png')

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 410
playerX_change = 0

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,100)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40


# player icon
def player(x,y):
    screen.blit(playerImg, (x,y))

#enemy icon
def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#main loop
while not done: 
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change=4
        enemyY+= enemyY_change
    elif enemyX >= 768:
        enemyX_change = -4
        enemyY+= enemyY_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
