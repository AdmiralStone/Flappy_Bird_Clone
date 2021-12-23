import pygame

#PyGame Variables
pygame.init()
screen = pygame.display.set_mode((576,1024))
runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()