#Importando as funcionalidades da biblioteca Pygame
import pygame as game


#Inicializando as funções do Pygame
game.init()


#Configurando tela, delta-time e título da janela
screen = game.display.set_mode((1280, 720))
clock = game.time.Clock()
game.display.set_caption('Chess Game')
font = game.font.Font('freesansbold.ttf', 20)

#Inicializando Loop de Gameplay
running = True


#Enquanto running for verdade mantenha o jogo em execução
while running:

    #Buscando eventos no frame
    for event in game.event.get():

        #Se evento for o de clicar para sair, saia do loop.
        if event.type == game.QUIT:
            running = False

    #Preencher a tela com a cor preta a cada loop
    screen.fill('black')
    screen.blit(font.render('Vamos iniciar um Jogo!', True, 'white'), (520,340))

    #Atualizar frame
    game.display.flip()


#Após sair do loop, saia do jogo.
game.quit()