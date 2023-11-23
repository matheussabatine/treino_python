import pygame as pg

class Ball():

    def __init__(self, screen):
        self.width= 15
        self.height= 15
        self.screen= screen
        self.shape= pg.Rect(self.screen.get_width()/2, self.screen.get_height()/2, self.width, self.height)
        self.vector= pg.Vector2(10, 0)

    def ball_move(self):
        self.shape.move_ip(self.vector)
        keys = pg.key.get_pressed()

            #girar bola
        if keys[pg.K_f]:
            self.vector.rotate_ip(180)

            #reflete quando toca a parede e chao
        if self.shape.top <= 0 or self.shape.bottom >= self.screen.get_height():
            self.vector.y *= -1

            #marcar gol
        #if self.shape.left <= 0 or self.shape.right >= self.screen.get_width():
            

    def ball_collider(self):
        self.vector.x *= -1
        
