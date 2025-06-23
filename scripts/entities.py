import pygame
import random

class Entity:
    def __init__(self, game, e_type, pos):
        self.game = game
        self.pos = list(pos)
        self.img = self.game.assets[e_type]

    def update(self, movement=(0, 0)):
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
    
    def render(self, surf, offset=(0, 0)):
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

class Ship(Entity):
    def __init__(self, game, pos):
        super().__init__(game, 'ship', pos)
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

class Bullet(Entity):
    def __init__(self, game, pos, velocity=(0, 0)):
        super().__init__(game, 'bullet', pos)
        self.velocity = velocity
    
    def update(self):
        super().update(self.velocity)

        # Check boundaries
        if self.pos[0] > self.game.display.get_width() or self.pos[0] < 0 or self.pos[1] > self.game.display.get_height() or self.pos[1] < 0:
            return True
        else:
            return False