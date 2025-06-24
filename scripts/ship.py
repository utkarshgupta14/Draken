import pygame

from scripts.entities import Entity
from scripts.bullets import Bullet

class Ship(Entity):
    def __init__(self, game, pos):
        super().__init__(game, pos, e_type='ship')
        self.shooting = False
        self.shooting_tick = 0
        
    def shoot(self, shooting):
        self.shooting = shooting
        self.shooting_tick = 0
    
    def update(self, movement=(0, 0)):
        super().update(movement=(movement[0]*3, movement[1]*3))

        if self.shooting:
            if self.shooting_tick%10 == 0:
                self.game.bullets.append(Bullet(self.game, (self.pos[0] + 15, self.pos[1] + 4), velocity=(0, -4 + movement[1]*0.5)))
            self.shooting_tick += 1