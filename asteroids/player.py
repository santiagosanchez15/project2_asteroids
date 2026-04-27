from circleshape import *
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
    
    def triangle(self): 
        '''Declare triangle'''
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: object):
        pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH )

    def rotate(self, dt):
        '''rotate the player by given dt value by the players speed'''
        self.rotation += PLAYER_TURN_SPEED * dt # speed times the value taken will equal to the amount of spaces that the triangle rotates
    
    def update(self, dt):
        '''Update value posision depending on the key pressed'''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # when the key a is pressed the dt is passed as a negative value becasue we want to turn left
            self.rotate( -dt)
        if keys[pygame.K_d]: #turn right when the key d is pressed and dt is passed as the value taken while holding the key
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        '''modifies players position'''

        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_speed_vector