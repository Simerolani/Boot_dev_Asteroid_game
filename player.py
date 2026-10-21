import pygame 
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: float, y: float)-> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface)-> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float)-> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float)-> None:
        unit_vektor = pygame.Vector2(0, 1)
        rotated_vektor = unit_vektor.rotate(self.rotation)
        rotated_and_speed_vektor = rotated_vektor * PLAYER_SPEED * dt
        self.position += rotated_and_speed_vektor
    
    def shoot(self)-> None:
        bullet = Shot(self.position.x, self.position.y)
        vektor = pygame.Vector2(0, 1)
        rotated_vektor = vektor.rotate(self.rotation)
        rotated_and_speed_vektor = rotated_vektor * PLAYER_SHOOT_SPEED
        bullet.velocity = rotated_and_speed_vektor
        self.cooldown += PLAYER_SHOOT_COOLDOWN_SECONDS

    def update(self, dt: float)-> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                self.cooldown -= dt
                if self.cooldown < 0:
                    self.cooldown = 0
            else:
                self.shoot()
        

