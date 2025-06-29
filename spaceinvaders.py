import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("space invaders game")
bg = pygame.image.load("space invaders/images/space.png")

velocity = 2
player1health = 10
player2health = 10

ship1 = pygame.image.load("space invaders/images/player1.png")
ship2 = pygame.image.load("space invaders/images/player2.png")
redship = pygame.transform.rotate(pygame.transform.scale(ship1, (60, 40)), 90)
yellowship = pygame.transform.rotate(pygame.transform.scale(ship2, (60, 40)), 270)

def drawwindow(red, yellow):
    screen.blit(bg, (0, 0))
    screen.blit(redship, (red.x, red.y))
    screen.blit(yellowship, (yellow.x, yellow.y))

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

def main():
    red = pygame.Rect(250, 250, 60, 40)
    yellow = pygame.Rect(750, 250, 60, 40)
    run = True
    while run:
        if red.x > 500:
            player1health -= 1
        if yellow.x < 500:
            player2health -= 1
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
               run = False
        keypress = pygame.key.get_pressed()
        yellowshipmovement(keypress, yellow)
        redshipmovement(keypress, red)
        drawwindow(red, yellow)
        pygame.display.update()

main()