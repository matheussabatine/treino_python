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
        self.max_vel= 12
        self.vector= pg.Vector2(self.vel, 0)
        self.angle_vector= pg.Vector2(1, 0) 

    def ball_move(self):
        self.last_position= self.position
        # cria algo para verificar quando bola for varar tela
        self.position.move_ip(self.vector)

        #reflete quando toca a parede e chao
        if self.position.top <= 0 or self.position.bottom >= self.screen.get_height():
            self.vector.reflect_ip((0, 1))
    
    def ball_collider_left(self, player_status):
        self.vector.x *= -1
        self.ball_acelerrate()
        #angle turn
        
        if player_status == 'moving_up' and self.vector.angle_to(self.angle_vector) + 10.00 < 40:
            #self.vector.rotate_ip(-30)
            self.vector.rotate_ip(-10)
        elif player_status == 'moving_down' and self.vector.angle_to(self.angle_vector) - 10.00 > -40:
            #self.vector.rotate_ip(30)
            self.vector.rotate_ip(10)
       
        #print(self.vector.angle_to(self.angle_vector))
    
    def ball_collider_right(self, player_status):
        self.vector.x *= -1
        self.ball_acelerrate()
        #angle turn
       
        
        if player_status == 'moving_up' and self.vector.angle_to(self.angle_vector) + 10.00 < 130:
            #self.vector.rotate_ip(30)
            self.vector.rotate_ip(10)
        elif player_status == 'moving_down' and self.vector.angle_to(self.angle_vector) - 10.00 > -130:
            #self.vector.rotate_ip(-30)
            self.vector.rotate_ip(-10)
        #print(self.vector.angle_to(self.angle_vector))
        
        
    def ball_acelerrate(self):
        if self.vector.x < self.max_vel and self.vector.x > 0:
            self.vector.x += 1
        elif self.vector.x > self.max_vel*-1 and self.vector.x < 0:
            self.vector.x += -1



    


    
