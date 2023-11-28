import pygame as pg
#from main import player_1, player_2, screen
import time
import random

class Ball_class():
    

    def __init__(self, screen):
        self.width= 15
        self.height= 15
        self.screen= screen
        self.position= pg.Rect(self.screen.get_width()/2, self.screen.get_height()/2, self.width, self.height)
        self.last_position= self.position
        self.vel= random.choice([4, -4])
        self.max_vel= 28
        self.vector= pg.Vector2(self.vel, 0)
        self.angles= {min:30, max:-30}

    def ball_move(self):
        self.last_position= self.position
        # cria algo para verificar quando bola for varar tela
        self.position.move_ip(self.vector)

            #reflete quando toca a parede e chao
        if self.position.top <= 0 or self.position.bottom >= self.screen.get_height():
            self.vector.y *= -1
          
    def ball_collider_left(self, player_status):
        self.vector.x *= -1
        self.ball_acelerrate()
        #angle turn
        if player_status == 'moving_up':
            self.vector.rotate_ip(-30)
        elif player_status == 'moving_down':
            self.vector.rotate_ip(30)

    def ball_collider_right(self, player_status):
        self.vector.x *= -1
        self.ball_acelerrate()
        #angle turn
        if player_status == 'moving_up':
            self.vector.rotate_ip(30)
        elif player_status == 'moving_down':
            self.vector.rotate_ip(-30)

        #speeding up the ball


    def ball_acelerrate(self):
        if self.vector.x < self.max_vel and self.vector.x > 0:
            self.vector.x += 1
        elif self.vector.x > self.max_vel*-1 and self.vector.x < 0:
            self.vector.x += -1



    


    
