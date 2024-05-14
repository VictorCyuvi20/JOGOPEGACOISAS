import pygame
from PG import*
pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))


#Criando mais personagens
griffith  = Personagem("imagens/griffith.webp",80,50,300,450)
guts = Personagem("imagens/guts.jpg",50,50,450,450)
objetos = Obstaculo = ("imagens/behelit.jpg",100,50,850,60)

