import circleshape as circ
import pygame as pyg
from constants import *
import random as r

class Asteroid(circ.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pyg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = r.uniform(20, 50) #Use random.uniform to generate a random angle between 20 and 50 degrees
        a1v = self.velocity.rotate(random_angle)
        a2v = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1v * 1.2
        a2.velocity = a2v * 1.2