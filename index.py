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

enemyNames = {0: "Roll", 1: "Troll", 2: "Tinder", 3: "Sem"}

level = 1
treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35, 40))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (35, 40))
enemyImage = enemyImage.convert_alpha()

enemyX = 50
enemyY = 450

treasureX = 450 - 35 / 2
treasureY = 50

screen.blit(treasureImage, (treasureX, treasureY))

playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (50, 60))
playerImage = playerImage.convert_alpha()
backGroundImage = pygame.image.load("background.png")
backGroundImage = pygame.transform.scale(backGroundImage, (900, 700))
screen.blit(backGroundImage, (0, 0))

frame = pygame.time.Clock()
collisionTeasure = False
collisionEnemy = False
movingRight = True

enemies = [(enemyX, enemyY, movingRight)]

while finished == False:
    for event in pygame.event.get():
        if event.type == 12:
            finished = False
    # black = (0, 0, 0)
    white = (255, 255, 255)
    screen.blit(backGroundImage, (0, 0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (x, y))

    enemyIndex = 0

    for enemyX, enemyY, movingRight in enemies:
        screen.blit(enemyImage, (enemyX, enemyY))
        collisionEnemy, y = checkCollision(x, y, enemyX, enemyY)
        if collisionEnemy == True:
            name = enemyNames[enemyIndex]
            textLose = font.render("You will kill by " + name, True, (255, 0, 0))
            screen.blit(textLose, (450 - textLose.get_width() / 2, 300 - textLose.get_height() / 2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(30)
        enemyIndex += 1



    collisionTeasure,y = checkCollision(x,y,treasureX,treasureY)

    rectOne = pygame.Rect(x, y, 30, 30)
    if collisionTeasure == True:
        level += 1
        enemies.append((enemyX - 50 * level, enemyY - 50 * level, False))
        textWin = font.render("Level up! Next level "+str(level), True, (0, 0, 0))
        screen.blit(textWin, (450 - textWin.get_width() / 2, 300 - textWin.get_height() / 2))
        pygame.display.flip()
        frame.tick(1)
    elif collisionEnemy == True:
        collisionEnemy = False


    pressedKeys = pygame.key.get_pressed()

    enemyIndex = 0
    for enemyX, enemyY, movingRight in enemies:
        if enemyX >= 815:
            movingRight = False
        elif enemyX <= 50:
            movingRight = True

        if movingRight == True:
            enemyX += 5*level
        else:
            enemyX -= 5*level
        enemies[enemyIndex] = (enemyX, enemyY, movingRight)
        enemyIndex += 1




    if pressedKeys[pygame.K_LEFT] == 1:
        x -= 5
    if pressedKeys[pygame.K_RIGHT] == 1:
        x += 5

    if pressedKeys[pygame.K_UP] == 1:
        y -= 5
    if pressedKeys[pygame.K_DOWN] == 1:
        y += 5

    color = (0, 0, 128)

    #    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()
    frame.tick(30)
