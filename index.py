import pygame


def checkCollision(x, y, treasureX, treasureY):
    global screen, textWin
    collisionState = False
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True

        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True

    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True

        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True
    return collisionState, y

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 450 - 35 / 2
y = 650


font = pygame.font.SysFont("comicsans", 60)
textWin = font.render("Yep,you win diamond!", True, (0, 0, 0))
treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35, 40))
treasureImage = treasureImage.convert_alpha()

treasureX = 450 - 35 / 2
treasureY = 50

screen.blit(treasureImage, (treasureX, treasureY))

playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage, (50, 60))
playerImage = playerImage.convert_alpha()
backGroundImage = pygame.image.load("background.png")
backGroundImage = pygame.transform.scale(backGroundImage, (900, 700))
screen.blit(backGroundImage, (0, 0))

while finished == False:
    for event in pygame.event.get():
        if event.type == 12:
            finished = False

    # black = (0, 0, 0)
    white = (255, 255, 255)
    screen.blit(backGroundImage, (0, 0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (x, y))
    collosionTeasure,y = checkCollision(x,y,treasureX,treasureY)

    rectOne = pygame.Rect(x, y, 30, 30)
    frame = pygame.time.Clock()
    collosionTeasure = True
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
    frame.tick(360)
