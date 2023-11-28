import pygame as pg

class Player():
   
    def __init__(self, xPosition, screen):
        self.height= round(screen.get_height()/6)
        self.width= round(self.height/4)
        self.screen= screen 
        self.vel= 500
        self.status= 'static'
       
        self.position= pg.Rect(xPosition, self.screen.get_height()/2, self.width, self.height)
        self.last_position= self.position

    def player_move(self, deltaTime, up_botton, down_botton):
        keys = pg.key.get_pressed()
        if keys[up_botton] and self.position.y >= 0:
            self.last_position= self.position
            self.position.y -= self.vel * deltaTime
            self.status= 'moving_up'
           
        elif keys[down_botton] and self.position.bottom <= self.screen.get_height():
            self.last_position= self.position
            self.position.y += self.vel * deltaTime
            self.status= 'moving_down'

        else:
            self.status= 'static'
           
        return self.last_position, self.position




