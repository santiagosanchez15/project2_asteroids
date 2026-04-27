from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import random

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return #if small enough kill
        log_event("asteroid_split")

        angle = random.uniform(20,50) #get random angle between given float
        vector = self.velocity.rotate(angle) #get new angle1
        vector2 = self.velocity.rotate(-angle) #get negaeive angle1
        new_radius = self.radius - ASTEROID_MIN_RADIUS #calculate the new radius
        as1 = Asteroid(self.position.x, self.position.y, new_radius) #create asteroid object1
        as1.velocity = vector * 1.2 # get new speed

        as2 = Asteroid(self.position.x, self.position.y, new_radius) #create asteroud object2
        as2.velocity = vector2 * 1.2 #get new speed
