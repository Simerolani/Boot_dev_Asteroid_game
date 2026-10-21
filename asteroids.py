import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int)-> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface)-> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float)-> None:
        self.position += self.velocity * dt

    def split(self)-> None:

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
 
        log_event("asteroid_split")
        new_vekt_1 = self.velocity.rotate(random.uniform(20, 50))
        new_vekt_2 = self.velocity.rotate(random.uniform(20, 50)*1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
 
        baby_1 = Asteroid(self.position.x, self.position.y, new_radius)
        baby_2 = Asteroid(self.position.x, self.position.y, new_radius)

        baby_1.velocity = new_vekt_1 * 1.2
        baby_2.velocity = new_vekt_2 * 1.2
        self.kill()
