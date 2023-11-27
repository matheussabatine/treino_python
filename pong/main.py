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
background.fill(grey)

# players and ball creation and playing buttons
player_1= Player(0, screen)
player_1_up=pg.K_w
player_1_down=pg.K_s

player_2= Player(screen.get_width() - player_1.width, screen)
player_2_up=pg.K_UP
player_2_down=pg.K_DOWN

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


#game loop
while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill parts of the screen with a color to wipe away anything from last frame
    background.fill(grey, player_1.last_position)
    background.fill(grey, player_2.last_position)
    background.fill(grey, ball.last_position)

    if ball.position.left <= 0:
        
        ball.goal(player_2, player_1, player_2, screen)
        del ball
        ball= Ball_class(screen)
     
    elif ball.position.right >= screen.get_width():
        
        ball.goal(player_1, player_1, player_2, screen)
        del ball
        ball= Ball_class(screen)
      
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
    print(ball.vector)

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