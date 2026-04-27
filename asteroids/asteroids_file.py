from circleshape import *
from constants import LINE_WIDTH

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, screen):
        '''Declare circle'''
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        '''upadte positoin of circle'''
        self.position += self.velocity * dt