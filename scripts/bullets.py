from scripts.entities import Entity

class Bullet(Entity):
    def __init__(self, game, pos, velocity=(0, 0)):
        super().__init__(game, pos, e_type='bullet')
        self.velocity = velocity
    
    def update(self):
        super().update(self.velocity)

        # Check boundaries
        if self.pos[0] > self.game.display.get_width() or self.pos[0] < 0 or self.pos[1] > self.game.display.get_height() or self.pos[1] < 0:
            return True
        else:
            return False