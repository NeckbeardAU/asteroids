import circleshape as circ
import constants as const
import pygame

class Player(circ.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, const.PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255,255,255), points, 2)