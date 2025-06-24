import pygame
import random
import math

from scripts.entities import Entity

class Astroid(Entity):
    def __init__(self, game, pos, velocity=(0, 0), variant=0):
        super().__init__(game, pos)
        self.img = self.game.assets['obstacles/astroids'][variant]
        self.angle = random.random() * math.pi * 2
        self.rotation_speed = random.random() * math.pi * 0.014 - math.pi * 0.007
        self.velocity = velocity
        self.size = self.img.get_size()
    
    def update(self):
        super().update(self.velocity)
        self.angle += self.rotation_speed
        self.angle = self.angle % (math.pi * 2)
        if self.pos[1] > self.game.display.get_size()[1]+100:
            return True
        return False
    
    def render(self, surf, offset=(0, 0)):
        rotated_img = pygame.transform.rotate(self.img, math.degrees(self.angle))
        rotated_rect = rotated_img.get_rect(center=(self.pos[0] - offset[0], self.pos[1] - offset[1]))
        surf.blit(rotated_img, rotated_rect.topleft)