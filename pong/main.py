import pygame as pg
import os
import time
from player import Player
from ball_file import Ball_class

# pygame setup
pg.init()

#colors
red= (255, 0, 0)
blue= (0, 0, 255)
grey= (107, 107, 107)
white= (255, 255, 255)
black= (0, 0, 0)

#screen
pg.display.set_caption ("PONG")
os.environ['SDL_VIDEO-CENTERED']= '1'
info = pg.display.Info()
monitor_width= info.current_w
monitor_height= info.current_h
#monitor full HD
if monitor_width >= 1920 and monitor_height >= 1080:
    width = 1820
    height = 950
#monitor 20 pol
elif monitor_width >= 1600 and monitor_height >= 900:
    width = 1440
    height = 800
#small monitor
else:
    width = 1200
    height = 700

screen = pg.display.set_mode((width, height))

#creating a surface with screen's size
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill(black)

# players and ball creation and playing buttons
player_1= Player(0, screen)
player_1_up=pg.K_w
player_1_down=pg.K_s
player_1_points= 0

player_2= Player(screen.get_width() - player_1.width, screen)
player_2_up=pg.K_UP
player_2_down=pg.K_DOWN
player_2_points= 0

ball= Ball_class(screen)
# hit(i use this to avoid the ball glitching inside the bat,verification at: ball_collision): 
# 0 = ball didn't hit the bat
# 1 = ball hitted the bat
hit= 0

# Blit everything to the screen
screen.blit(background, (0, 0))
#render everything
pg.display.flip()

# clock and game running = True
running = True
clock = pg.time.Clock()
deltaTime = clock.tick(100) / 1000

#Functions

def ball_restart():
     global ball
     global player_1
     global player_2
     del ball
     del player_1
     del player_2
     player_1= Player(0, screen)
     player_2= Player(screen.get_width() - player_1.width, screen)
     ball= Ball_class(screen)

def goal(point):
        global player_1_points
        global player_2_points
        global screen
        white= (255, 255, 255)
        if point == 'player1':
            player_1_points+=1
        else:
            player_2_points+=1
        my_font = pg.font.Font('thirdparty\\fonts\\DS-DIGI.TTF', 100)
        text_surface_left = my_font.render('{}'.format(player_1_points), False, white)
        text_surface_right = my_font.render('{}'.format(player_2_points), False, white)
        screen.blit(text_surface_left, (screen.get_width()*1/4, 5))
        screen.blit(text_surface_right, (screen.get_width()*3/4, 5))
        pg.display.update()
        time.sleep(3)

#game loop
while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill parts of the screen with a color to wipe away anything from last frame
    background.fill(black, player_1.last_position)
    background.fill(black, player_2.last_position)
    background.fill(black, ball.last_position)

    #goal

    if ball.position.left <= 0 or ball.position.right >= screen.get_width():
        if ball.position.left <= 0:
             goal('player2')
        else:
             goal('player1')
        ball_restart()
     
# PHISICS
    #move the players
    player_1.player_move(deltaTime, player_1_up, player_1_down )
    player_2.player_move(deltaTime, player_2_up, player_2_down )
    
    #ball collision at players
    ball_collision= pg.Rect.colliderect(ball.position, player_1.position) or pg.Rect.colliderect(ball.position, player_2.position)
    
    if ball_collision== True and hit== 0:
            if ball.position.x < background.get_width()/2:
                ball.ball_collider_left(player_1.status)
            else:
                ball.ball_collider_right(player_2.status) 
            hit= 1
    elif ball_collision== False and hit== 1:
            hit= 0  
    ball.ball_move()

# END OF PHISICS
    
    #redraw the players, and ball on the the surface 'background'
    pg.draw.rect(background, blue, player_1.position)
    pg.draw.rect(background, red, player_2.position)
    pg.draw.rect(background, white, ball.position)

    # update() the display to put your work on screen
    screen.blit(background, (0, 0))
    pg.display.update()

    # FPS limiter
    clock.tick(100)

pg.quit()