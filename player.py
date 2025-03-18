from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius): #do i need to add player radius here? THinking nosince it's a constant pulled from constants file
        super().__init__(x, y, radius)
    rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        return super().draw(screen) #this line was auto-generated, not sure if it is needed?
    
