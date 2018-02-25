import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False


while finished == False:
    for event in pygame.event.get():
        if pygame.QUIT == 12:
            finished = True

    rectOne = pygame.Rect(0, 0, 300, 300)

    color = (0, 0, 128)

    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()


