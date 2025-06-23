import pygame
import sys
import random
import math

from scripts.entities import Entity, Ship, Bullet
from scripts.utils import *

class Game:
    def __init__(self):
        # basic setup
        pygame.init()
        pygame.display.set_caption("Rokzor")
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1280, 800))
        self.display = pygame.Surface((640, 400))

        # [L, R, U, D]
        self.movement = [False, False, False, False]

        # game assets
        self.assets = {
            'ship' : load_image('ship.png'),
            'bullet' : load_image('bullet.png'),
        }

        self.ship = Ship(self, (304, 300))

        self.bullets = []

    def run(self):
        while True:
            # render background
            self.display.fill((0, 0, 0))

            # render player
            self.ship.update((self.movement[1]-self.movement[0], self.movement[3]-self.movement[2]))
            self.ship.render(self.display)

            # render bullets
            for bullet in self.bullets.copy():
                kill = bullet.update()
                if kill:
                    self.bullets.remove(bullet)
                else:
                    bullet.render(self.display)

            # game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    if event.key == pygame.K_SPACE:
                        self.ship.shoot(True)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False
                    if event.key == pygame.K_SPACE:
                        self.ship.shoot(False)
   
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()