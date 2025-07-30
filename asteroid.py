import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            asteroid1_velocity = self.velocity.rotate(angle) * 1.2
            asteroid2_velocity = self.velocity.rotate(-angle) * 1.2

            new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
            new_asteroid1.velocity = asteroid1_velocity
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
            new_asteroid2.velocity = asteroid2_velocity
        