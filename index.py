import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 450-35/2
y = 645

playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage,(50, 60))
playerImage = playerImage.convert_alpha()
backGroundImage = pygame.image.load("background.png")
backGroundImage = pygame.transform.scale(backGroundImage, (900, 700))
screen.blit(backGroundImage,(0,0))


while finished == False:
    for event in pygame.event.get():
        if event.type == 12:
            finished = False

    #black = (0, 0, 0)
    white = (255, 255, 255)
    screen.blit(backGroundImage, (0, 0))
    screen.blit(playerImage, (x, y))
    rectOne = pygame.Rect(x, y, 30, 30)
    frame = pygame.time.Clock()
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

#    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()
    frame.tick(60)
