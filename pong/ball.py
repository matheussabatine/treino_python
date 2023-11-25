import pygame as pg

class Ball():

    def __init__(self, screen):
        self.width= 15
        self.height= 15
        self.screen= screen
        self.position= pg.Rect(self.screen.get_width()/2, self.screen.get_height()/2, self.width, self.height)
        self.last_position= self.position
        self.vel= 10
        self.vector= pg.Vector2(self.vel, 0)
        self.maxAngle= [30, -30]

    def ball_move(self):
        self.last_position= self.position
        # cria algo para verificar quando bola for varar tela
        self.position.move_ip(self.vector)
        keys = pg.key.get_pressed()

            #reflete quando toca a parede e chao
        if self.position.top <= 0 or self.position.bottom >= self.screen.get_height():
            self.vector.y *= -1

    def ball_goal(self, player):
        player.points += 1
        #if self.position.left <= 0 or self.position.right >= self.screen.get_width():
            

    def ball_collider(self):
        self.vector.x *= -1
        if self.vector.x > 0:
            self.vector.x += 5
        else:
            self.vector.x -= 5

      #rotate ball
    def ball_rotate(self):
        self.vector.rotate_ip(30)

        
