import pygame

pygame.init()
win = pygame.display.set_mode((618, 359))
# Вызов окна с игрой

pygame.display.set_caption("Poweroff game")
# Заголовок окна

walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'),
pygame.image.load('right_3.png'), pygame.image.load('right_4.png'),
pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'),
pygame.image.load('left_3.png'), pygame.image.load('left_4.png'),
pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

fon = pygame.image.load('fon.png')
# Load fon
playerStand = pygame.image.load('idle.png')
# Load pic gamer


clock = pygame.time.Clock()

x = 50
y = 300
width = 46
height = 56
speed = 5
# Igrok
isJump = False
jumpCount = 10
# Prizhok

left = False
rigth = False
animCount = 0

def drawWindow():
    global animCount # Ssilka na global peremennya
    win.blit(fon, (0, 0)) #Zakrashivanie okna

    if animCount + 1 >= 30:         #Frame in sec
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif rigth:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    # Opisanie animation (risuem igroka)


    pygame.display.update()  #Obnovlenie okna

run = True
while run:
    # pygame.time.delay(30) #Vremya vipolneniya zikla (Skorost irgi)
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# Proverka na zakritie okna

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        rigth = False
    elif keys[pygame.K_RIGHT] and x < 618 - width - 5:
        x += speed
        left = False
        rigth = True
    else:
        left = False
        rigth = False
        animCount = 0
    if not(isJump): # Func if prizhok, to not up and down


        # if keys[pygame.K_UP] and y > 5:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 500 - height - 5:
        #     y += speed
        # Up and Down igroka
# Rabota knopok i ramki igri
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
# Opisanie raboty prizka

    drawWindow() #Vyzov func


    # win.fill((0,0,0)) #Zakrashivanie okna chernym
    # pygame.draw.rect(win, (0,0,255), (x, y, width, height))  #Igrok
    # pygame.display.update()  #Obnovlenie okna


pygame.quit()
