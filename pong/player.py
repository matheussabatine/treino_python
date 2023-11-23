import pygame as pg

class Player():
   
    def __init__(self, xPosition, screen):
        self.height= round(screen.get_height()/6)
        self.width= round(self.height/4)
        self.screen= screen 
        self.vel= 600
       
        self.shape= pg.Rect(xPosition, self.screen.get_height()/2, self.width, self.height)

    def player_move(self, deltaTime, up_botton, down_botton):
        keys = pg.key.get_pressed()
        if keys[up_botton] and self.shape.y >= 0:
            self.shape.y -= self.vel * deltaTime
        if keys[down_botton] and self.shape.bottom <= self.screen.get_height():
            self.shape.y += self.vel * deltaTime
        
        return self.shape.y




