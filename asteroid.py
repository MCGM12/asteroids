import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        newAngle = random.uniform(20, 50)

        a1 = self.velocity.rotate(newAngle)
        a2 = self.velocity.rotate(-newAngle)

        new_Radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_Radius)
        asteroid.velocity = a1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_Radius)
        asteroid.velocity = a2 * 1.2
            
