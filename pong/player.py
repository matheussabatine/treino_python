import pygame as pg

class Player():
   
    def __init__(self, xPosition, screen):
        self.height= round(screen.get_height()/6)
        self.width= round(self.height/4)
        self.screen= screen 
        self.vel= 700
        self.points= 0
       
        self.position= pg.Rect(xPosition, self.screen.get_height()/2, self.width, self.height)
        self.last_position= self.position

    def player_move(self, deltaTime, up_botton, down_botton):
        keys = pg.key.get_pressed()
        if keys[up_botton] and self.position.y >= 0:
            self.last_position= self.position
            self.position.y -= self.vel * deltaTime
           
        elif keys[down_botton] and self.position.bottom <= self.screen.get_height():
            self.last_position= self.position
            self.position.y += self.vel * deltaTime
           
        return self.last_position, self.position




