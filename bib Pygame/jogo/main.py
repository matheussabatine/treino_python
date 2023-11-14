import pygame
import os

WIDTH, HEIGHT=900, 500
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
AZUL= (34, 43, 110)

FPS= 60
#titulo da janela
NAVE_LARGURA, NAVE_ALTURA= 55, 40
pygame.display.set_caption("jogo de nave")

NAVE_AMARELA_IMAGEM= pygame.image.load(os.path.join('jogo', 'Assets', 'spaceship_yellow.png'))
NAVE_AMARELA= pygame.transform.scale(NAVE_AMARELA_IMAGEM, (NAVE_LARGURA, NAVE_ALTURA))
NAVE_VERMELHA_IMAGEM= pygame.image.load(os.path.join('jogo', 'Assets', 'spaceship_red.png'))
NAVE_VERMELHA= pygame.transform.scale(NAVE_VERMELHA_IMAGEM, (NAVE_LARGURA, NAVE_ALTURA))

def draw_window():
    WIN.fill(AZUL)
    WIN.blit(NAVE_AMARELA_IMAGEM, (300, 100))
    #tem que atualizar a tela
    pygame.display.update()

def main():
    clock= pygame.time.Clock()
    run= True
    while run:
        #limita o fps
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        draw_window()

    pygame.quit()

#roda a função main apenas se rodar este arquivo
if __name__ == "__main__":
    main()