import pygame
from pygame.locals import *
from sys import exit
from random import randint

la = 880
al = 840
x = -30
y = 500

x_azul = 1
y_azul = randint(268,700)

x_roxo = 1
y_roxo = randint(268, 700)

x_amarelo = 1
y_amarelo = randint(268,700)


pygame.init()
pontos = 0

tela = pygame.display.set_mode((la, al))
relogio = pygame.time.Clock()
fundo = pygame.image.load(f"C:/Users/Cliente/Documents/GitHub/TheCarGame---Ot-vio-Tavares")
velocidade_y = 8
tempo = 10
velocidade = 5
while True:
    fonte = pygame.font.SysFont("arial", 40, True, True)
    mensagem = f"pontos: {pontos}"
    texto = fonte.render(mensagem, True, (255,0,0))
    tela.fill((0, 255, 81))
    tela.blit(texto, (70,50))
    relogio.tick(60)
    tela.blit(fundo, (0, 91))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_w]:
        if y <= 268:
            pass
        else:
            y = y - velocidade_y
    if pygame.key.get_pressed()[K_a]:
        if x < 0:
            pass
        else:
            x = x - 10
    if pygame.key.get_pressed()[K_s]:
        if y >= 700:
            pass
        else:
            y = y + velocidade_y

    player = pygame.draw.rect(tela, (255, 0, 0), (x, y , 70, 30))
    car_roxo = pygame.draw.rect(tela, (127, 0, 255), (x_roxo, y_roxo, 70, 30))
    car_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 70, 30))
    car_amarelo = pygame.draw.rect(tela, (255, 247, 0), (x_amarelo, y_amarelo, 70, 30))
    if player.colliderect(car_azul) or player.colliderect(car_amarelo):
        pontos = pontos - 1
    if pontos < 0:
        pontos = 0

    x_roxo = x_roxo + 4.5 + pontos + 6
    x_azul = x_azul + 4.5 + pontos +6
    x_amarelo = x_amarelo + 4.5 + pontos +6
    x = x + 2.5 + pontos + 2

    if x > la:
        x = -40
        x += 1 +19
        pontos += 1
       # tela.blit(texto, (70, 50))

    if x_azul > la:
        x_azul = -30
        y_azul = randint(268, 700)
        x_azul += 0

    if x_amarelo > la:
        x_amarelo = -30
        y_amarelo = randint(268, 700)
        x_amarelo += 0

    if x_roxo > la:
        x_roxo = -30
        y_roxo = randint(268, 700)
        x_roxo += 0

    pygame.display.update()