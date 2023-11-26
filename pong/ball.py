import pygame as pg

class Ball():

    def __init__(self, screen):
        self.width= 15
        self.height= 15
        self.screen= screen
        self.position= pg.Rect(self.screen.get_width()/2, self.screen.get_height()/2, self.width, self.height)
        self.last_position= self.position
        self.vel= 4
        self.max_vel= 20
        self.vector= pg.Vector2(self.vel, 0)
        self.angle= 0
        self.angles= {min:30, max:-30}

    def ball_move(self):
        self.last_position= self.position
        # cria algo para verificar quando bola for varar tela
        self.position.move_ip(self.vector)

            #reflete quando toca a parede e chao
        if self.position.top <= 0 or self.position.bottom >= self.screen.get_height():
            self.vector.y *= -1
            #if self.vector.y > 

    def ball_goal(self, player):
        player.points += 1
        #if self.position.left <= 0 or self.position.right >= self.screen.get_width():
            
    def ball_collider(self, player_status):
        self.vector.x *= -1
        #angle turn
        if self.angle < self.angles[min] and player_status == 'moving_up':
            self.vector.rotate_ip(-30)
            self.angle += 30
        elif self.angle > self.angles[max] and player_status == 'moving_down':
            self.vector.rotate_ip(30)
            self.angle -= 30

        #speeding up the ball
        if self.vector.x<self.max_vel:
            if self.vector.x > 0:
                self.vector.x += 1
            else:
                self.vector.x -= 1
