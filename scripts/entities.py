import pygame
import random

class Entity:
    def __init__(self, game, pos, e_type = None):
        self.game = game
        self.pos = list(pos)
        if e_type is not None:
            self.img = self.game.assets[e_type]

    def update(self, movement=(0, 0)):
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
    
    def render(self, surf, offset=(0, 0)):
        if self.img is not None:
            surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))