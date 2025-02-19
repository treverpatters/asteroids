from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(ASTEROID_SPLIT_MIN, ASTEROID_SPLIT_MAX)
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_half = Asteroid(self.position.x, self.position.y, new_radius)
        first_half.velocity = first_vector * 1.2
        second_half = Asteroid(self.position.x, self.position.y, new_radius)
        second_half.velocity = second_vector * 1.2

        

        