import pygame
from PG import*
from OG import*
from MB import*
from gp import*

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/inferno.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
guts = Personagem("imagens/guts.jpg",100,100,0,400)
griffith = Griffith("imagens/griffith.webp",80,80,0,0)
lista_behelit = [Obstaculo("imagens/behelit.jpg",50,80,0,0),Obstaculo("imagens/behelit.jpg",50,80,0,0),
                    Obstaculo("imagens/behelit.jpg",50,80,0,0),Obstaculo("imagens/behelit.jpg",50,80,0,0)]
                    
lista_behelit2 = [Obstaculo("imagens/behelit2.jpg",50,80,200,200 ), Obstaculo("imagens/behelit2.jpg",50,80,200,200 ), Obstaculo("imagens/behelit2.jpg",50,80,200,200 )]

lista_cruz = [Obstaculo("imagens/cruz.webp",50,80,0,0 ), Obstaculo("imagens/cruz.webp",50,80,0,0 ), Obstaculo("imagens/cruz.webp",50,80,0,0 ),
                  Obstaculo("imagens/cruz.webp",50,80,0,0 ), Obstaculo("imagens/cruz.webp",50,80,0,0 )]


#Configurando a fonte
fonte = pygame.font.SysFont("Castellar",18)


#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()

rodando = True
pontuacao=0
while rodando:
    
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
    

    tela.blit(FUNDO,(0,0))

    #Desenhando as imagens
    guts.movimenta_via_controle(pygame.K_d, pygame.K_a)
    guts.desenhar(tela)

    griffith.movimenta()
    griffith.apareca(tela)

    for OG in lista_behelit:
        OG.movimenta()
        OG.apareca(tela)
        if guts.mascara.overlap(OG.mascara,(OG.pos_x - guts.pos_x,  OG.pos_y- guts.pos_y)):
            pontuacao = pontuacao + 1
            OG.pos_x= 1000
            OG.pos_y= OG.pos_y

    for OG in lista_cruz:
        OG.movimenta()
        OG.apareca(tela)
        if guts.mascara.overlap(OG.mascara,(OG.pos_x - guts.pos_x,  OG.pos_y- guts.pos_y)):
            pontuacao = pontuacao + 3
            OG.pos_x= 1000
            OG.pos_y= OG.pos_y


            
    for OG in lista_behelit2:
        OG.movimenta()
        OG.apareca(tela)
        if guts.mascara.overlap(OG.mascara,(OG.pos_x - guts.pos_x,  OG.pos_y- guts.pos_y)):
            rodando = False

    for MB in lista_behelit:
        MB.movimenta()
        MB.apareca(tela)

    texto_ponto_guts = fonte.render(f"PONTUAÇÃO DA GUTS: {pontuacao}", False,(0,255,0))
    tela.blit(texto_ponto_guts,(0,10))


    
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)
