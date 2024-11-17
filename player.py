import circleshape as circ
import constants as const
import pygame as pyg
import shots as sh

class Player(circ.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, const.PLAYER_RADIUS)
        self.rotation = 0




    def triangle(self):
        forward = pyg.Vector2(0, 1).rotate(self.rotation)
        right = pyg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pyg.draw.polygon(screen, (255,255,255), points, 2)

    def rotate(self, dt):
        self.rotation += (const.PLAYER_TURN_SPEED * dt)
 

    def update(self, dt):
        keys = pyg.key.get_pressed()

        if keys[pyg.K_d]:
            self.rotate(dt)
        if keys[pyg.K_a]:
            self.rotate(-dt)
        if keys[pyg.K_w]:
            self.move(dt)
        if keys[pyg.K_s]:
            self.move(-dt)
        if keys[pyg.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pyg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * const.PLAYER_SPEED * dt

    def shoot(self):

        direction = pyg.Vector2(0, 1).rotate(self.rotation)
        shoot = sh.Shot(self.position.x, self.position.y, const.SHOT_RADIUS) #create the shot object
        direction *= const.PLAYER_SHOOT_SPEED #multiply the vector by the shoot speed so that its moving at the right speed
        shoot.velocity = direction #Set the velocity of the object 
          

