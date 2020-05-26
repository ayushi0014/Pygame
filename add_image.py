import pygame
pygame.init()

white = (255, 255, 255)
height = 400
width = 400
display_surface = pygame.display.set_mode((height, width))
pygame.display.set_caption('Image')

image = pygame.image.load(r'C:\Users\Ayushi Sharma\Desktop\Pygame\src\download.jpg')
image_small = pygame.transform.scale(image,(300,300))

while True: 
    display_surface.fill(white)
    display_surface.blit(image_small, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()        
