import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
   
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # No new Asteroid
        else:
            angle = random.uniform(20,50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            
            first_vector = self.velocity.rotate(angle)
            first_vector *= 1.2
            first_asteroid = Asteroid(self.position.x, self.position.y, radius)
            first_asteroid.velocity = first_vector

            second_vector = self.velocity.rotate(-angle) 
            second_vector *= 1.2
            second_asteroid = Asteroid(self.position.x, self.position.y, radius)
            second_asteroid.velocity = second_vector
            
            return first_asteroid, second_asteroid

