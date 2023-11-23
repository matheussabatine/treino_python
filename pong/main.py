import pygame as pg
import os
from player import Player
from ball import Ball

# pygame setup
pg.init()

#colors
red= (255, 0, 0)
blue= (0, 0, 255)
black= (0, 0, 0)
white= (255, 255, 255)

#screen
pg.display.set_caption ("PONG")
os.environ['SDL_VIDEO-CENTERED']= '1'
info = pg.display.Info()
monitor_width= info.current_w
monitor_height= info.current_h
#monitor full HD
if monitor_width >= 1920 and monitor_height >= 1080:
    width = 1820
    height = 980
#monitor 20 pol
elif monitor_width >= 1600 and monitor_height >= 900:
    width = 1440
    height = 800
#small monitor
else:
    width = 1200
    height = 700

screen = pg.display.set_mode((width, height))

running = True
clock = pg.time.Clock()
deltaTime = clock.tick(100) / 1000

# players and ball creation and buttons

player_1= Player(0, screen)
player_1_up=pg.K_w
player_1_down=pg.K_s

player_2= Player(screen.get_width() - player_1.width, screen)
player_2_up=pg.K_UP
player_2_down=pg.K_DOWN

ball= Ball(screen)

hit= 1


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
    
    # PHISICS
    #move the players
    player_1.player_move(deltaTime, player_1_up, player_1_down )
    player_2.player_move(deltaTime, player_2_up, player_2_down )

    #ball collision at players
    ball_collision= pg.Rect.colliderect(ball.shape, player_1.shape) or pg.Rect.colliderect(ball.shape, player_2.shape)
    if ball_collision== True and hit== 1:
            ball.ball_collider()
            hit= 0
    elif ball_collision== False and hit== 0:
            hit= 1 
       
    ball.ball_move()

    # END OF PHISICS

    # update() the display to put your work on screen
    pg.display.update()

    # FPS limiter
    clock.tick(100)

pg.quit()