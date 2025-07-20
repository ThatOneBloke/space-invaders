import pygame
import os
import time
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("space invaders game")
bg = pygame.image.load("space invaders/images/space.png")

fps = 60
bulletvelocity = 7
velocity = 2
player1health = 10
player2health = 10
yellowhit = pygame.USEREVENT + 1
redhit = pygame.USEREVENT + 2

ship1 = pygame.image.load("space invaders/images/player1.png")
ship2 = pygame.image.load("space invaders/images/player2.png")
redship = pygame.transform.rotate(pygame.transform.scale(ship1, (60, 40)), 90)
yellowship = pygame.transform.rotate(pygame.transform.scale(ship2, (60, 40)), 270)

def drawwindow(red, yellow, redbullet, yellowbullet, player1health, player2health):
    #global player1health, player2health
    screen.blit(bg, (0, 0))
    screen.blit(redship, (red.x, red.y))
    screen.blit(yellowship, (yellow.x, yellow.y))
    for i in redbullet:
        pygame.draw.rect(screen, "red", i)
    for i in yellowbullet:
        pygame.draw.rect(screen, "yellow", i)
    font1 = pygame.font.SysFont("Ariel", 20)
    text1 = font1.render("player1 health = " + str(player1health), True, "white")
    screen.blit(text1, (20, 20))
    text2 = font1.render("player2 health = " + str(player2health), True, "white")
    screen.blit(text2, (860, 20))
    pygame.display.update()
    if player1health == 0:
            screen.fill("yellow")
            wintext1 = font1.render("yellow has won!!!", True, "black")
            screen.blit(wintext1, (500, 250))
            pygame.display.update()
            time.sleep(20)
            quit()
    if player2health == 0:
            screen.fill("red")
            wintext2 = font1.render("red has won!!!", True, "black")
            screen.blit(wintext2, (500, 250))
            pygame.display.update()
            time.sleep(20)
            quit()
def redshipmovement(keypress, red):
    if keypress[pygame.K_a]:
        red.x -= velocity
    if keypress[pygame.K_s]:
        red.y += velocity
    if keypress[pygame.K_d]:
        red.x += velocity
    if keypress[pygame.K_w]:
        red.y -= velocity

def yellowshipmovement(keypress, yellow):
    if keypress[pygame.K_LEFT]:
        yellow.x -= velocity
    if keypress[pygame.K_DOWN]:
        yellow.y += velocity
    if keypress[pygame.K_RIGHT]:
        yellow.x += velocity
    if keypress[pygame.K_UP]:
        yellow.y -= velocity

def handlebullets(yellowbullet, redbullet, yellow, red):
    global player1health, player2health
    for i in yellowbullet:
        i.x -= bulletvelocity
        if red.colliderect(i):
            yellowbullet.remove(i)
            pygame.event.post(pygame.event.Event(redhit))
            pygame.display.update()
            time.sleep(0.01)
            player1health -= 1
    for i in redbullet:
        i.x += bulletvelocity
        if yellow.colliderect(i):
            redbullet.remove(i)
            pygame.event.post(pygame.event.Event(yellowhit))
            pygame.display.update()
            time.sleep(0.01)
            player2health -= 1

    pygame.display.update()
    time.sleep(0.01)

def main():
    global player1health, player2health
    red = pygame.Rect(250, 250, 60, 40)
    yellow = pygame.Rect(750, 250, 60, 40)
    run = True
    yellowbullet = []
    redbullet = []
    while run:
        if red.x > 500:
            player1health -= 1
            red.x = 250
        if yellow.x < 500:
            player2health -= 1
            yellow.x = 750
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
               run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 2, 20, 10)
                    redbullet.append(bullet)
                if i.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(yellow.x - yellow.width, yellow.y + yellow.height//2 - 2, 20, 10)
                    yellowbullet.append(bullet)
        keypress = pygame.key.get_pressed()
        yellowshipmovement(keypress, yellow)
        redshipmovement(keypress, red)
        handlebullets(yellowbullet, redbullet, yellow, red)
        drawwindow(red, yellow, redbullet, yellowbullet, player1health, player2health)
        pygame.display.update()

main()