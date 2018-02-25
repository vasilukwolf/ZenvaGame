import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 0
y = 50

# print pygame.K_SPACE

while finished == False:
    for event in pygame.event.get():
        if event.type == 12:
            finished = False

    black = (0, 0, 0)
    screen.fill(black)
    rectOne = pygame.Rect(x, y, 30, 30)

    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_LEFT] == 1:
        x -= 1
    if pressedKeys[pygame.K_RIGHT] == 1:
        x += 1

    if pressedKeys[pygame.K_UP] == 1:
        y -= 1
    if pressedKeys[pygame.K_DOWN] == 1:
        y += 1

    color = (0, 0, 128)

    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()
