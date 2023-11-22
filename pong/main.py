# Example file showing a circle moving on screen
import pygame as pg
from player import Player
from ball import Ball

# pygame setup
pg.init()

#colors
red= (255, 0, 0)
blue= (0, 0, 255)
black= (0, 0, 0)
white= (255, 255, 255)

#screen size
pg.display.set_caption ("PONG")
width= 1280
height= 720
screen = pg.display.set_mode((width, height))

running = True
clock = pg.time.Clock()
deltaTime = clock.tick(60) / 1000

# players and ball creation and buttons
player_reference= Player(0, screen)

player_1= Player(0, screen)
player_1_up=pg.K_w
player_1_down=pg.K_s

player_2= Player(width - player_reference.width, screen)
player_2_up=pg.K_UP
player_2_down=pg.K_DOWN

ball= Ball(screen)

#game mechanics


#jogador= pg.Rect(0, screen.get_height()/2, 30, 150)

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(black)

    #draw the players, and ball
    pg.draw.rect(screen, blue, player_1.shape)
    pg.draw.rect(screen, red, player_2.shape)
    pg.draw.rect(screen, white, ball.shape)
    
    #move the players
    player_1.player_move(deltaTime, player_1_up, player_1_down )
    player_2.player_move(deltaTime, player_2_up, player_2_down )

    if pg.Rect.colliderect(ball.shape, player_1.shape):
        print("due")
    
    ball.ball_move()

    # update() the display to put your work on screen
    pg.display.update()

    # FPS limiter
    clock.tick(60)

pg.quit()