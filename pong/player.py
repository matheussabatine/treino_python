import pygame as pg

class Player():
   
    def __init__(self, xPosition, screen):
        self.width= 30
        self.height= 150
        self.screen= screen 
        self.vel= 600
       
        self.shape= pg.Rect(xPosition, self.screen.get_height()/2, self.width, self.height)

    def player_move(self, deltaTime, up_botton, down_botton):
        keys = pg.key.get_pressed()
        if keys[up_botton] and self.shape.y >= 0:
            self.shape.top -= self.vel * deltaTime
        if keys[down_botton] and self.shape.bottom <= self.screen.get_height():
            self.shape.y += self.vel * deltaTime
        
        return self.shape.y




