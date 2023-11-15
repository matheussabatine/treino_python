import pygame
import os

WIDTH, HEIGHT=900, 500
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
AZUL= (34, 43, 110)
PRETO= (0, 0, 0)

FRONTEIRA= pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS= 60
VEL= 5
#titulo da janela
NAVE_LARGURA, NAVE_ALTURA= 55, 40
pygame.display.set_caption("jogo de nave")

NAVE_AMARELA_IMAGEM= pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
NAVE_AMARELA= pygame.transform.rotate(pygame.transform.scale(NAVE_AMARELA_IMAGEM, (NAVE_LARGURA, NAVE_ALTURA)),90)

NAVE_VERMELHA_IMAGEM= pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
NAVE_VERMELHA= pygame.transform.rotate(pygame.transform.scale(NAVE_VERMELHA_IMAGEM, (NAVE_LARGURA, NAVE_ALTURA)),-90)

def draw_window(VERMELHA, AMARELA):
    WIN.fill(AZUL)
    pygame.draw.rect(WIN, PRETO, FRONTEIRA)
    WIN.blit(NAVE_AMARELA, (AMARELA.x, AMARELA.y))
    WIN.blit(NAVE_VERMELHA, (VERMELHA.x, VERMELHA.y))
    #tem que atualizar a tela
    pygame.display.update()
def amarela_movimento(TECLAS_PRESSIONADAS, AMARELA):
    if TECLAS_PRESSIONADAS[pygame.K_a] and AMARELA.x - VEL > 0: #esquerda
            AMARELA.x += -VEL

    if TECLAS_PRESSIONADAS[pygame.K_d] and AMARELA.x + AMARELA.width + VEL < FRONTEIRA.x: #direita
            AMARELA.x += VEL

    if TECLAS_PRESSIONADAS[pygame.K_w] and AMARELA.y - VEL > 0: #cima
            AMARELA.y += -VEL

    if TECLAS_PRESSIONADAS[pygame.K_s] and AMARELA.y + AMARELA.height + VEL < HEIGHT: #baixo
            AMARELA.y += VEL

def vermelha_movimento(TECLAS_PRESSIONADAS, VERMELHA):
    if TECLAS_PRESSIONADAS[pygame.K_LEFT] and VERMELHA.x - VEL > FRONTEIRA.x + FRONTEIRA.width: #esquerda
            VERMELHA.x += -VEL

    if TECLAS_PRESSIONADAS[pygame.K_RIGHT] and VERMELHA.x + VERMELHA.width + VEL < WIDTH: #direita
            VERMELHA.x += VEL

    if TECLAS_PRESSIONADAS[pygame.K_UP] and VERMELHA.y - VEL > 0: #cima
            VERMELHA.y += -VEL

    if TECLAS_PRESSIONADAS[pygame.K_DOWN] and VERMELHA.y + VERMELHA.height + VEL < HEIGHT: #baixo
            VERMELHA.y += VEL

def main():
    VERMELHA= pygame.Rect(700,300, NAVE_LARGURA, NAVE_ALTURA)
    AMARELA= pygame.Rect(100,300, NAVE_LARGURA, NAVE_ALTURA)

    clock= pygame.time.Clock()
    run= True
    while run:
        #limita o fps
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        TECLAS_PRESSIONADAS= pygame.key.get_pressed()
        amarela_movimento(TECLAS_PRESSIONADAS, AMARELA)
        vermelha_movimento(TECLAS_PRESSIONADAS, VERMELHA)
       

        draw_window(VERMELHA, AMARELA)

    pygame.quit()

#roda a função main apenas se rodar este arquivo
if __name__ == "__main__":
    main()