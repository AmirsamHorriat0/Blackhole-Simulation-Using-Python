import pygame
import random
import math

#Windows Size
WIDTH , HEIGHT = 900 , 900

#center point
CENTERPOINT = WIDTH // 2 , HEIGHT // 2

#gravitational constant
G = 2000

#time step used in integration
DT = 0.01

#number of orbiting stars
NUM_PARTICLE = 250


'''
now we need a particle object which will define the x,y ( positions ) and vx , vy 
( velocities )
'''

class Particle:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        #Color
        self.color = (200 , 200 , 255)

        #Radius
        self.size = 2

    #computing the gravitational acceleration
    def update(self , blackhole) :
        dx = blackhole.x - self.x
        dy = blackhole.y - self.y
        r = math.sqrt(dx ** 2 + dy ** 2)

        # r is the distance between the particle and the center of the black hole.
        # So that if the particle moves inside the black hole it should get delete.
        if r < blackhole.radius :
            return False

        #Newton’s law of universal gravitation

        # x direction
        ax = G * dx / r**3

        # y direction
        ay = G * dy / r**3

        # Velocity update
        # velocity increases in the direction of gravity
        # the closer the particle gets, the stronger the pull
        self.vx += ax * DT
        self.vy += ay * DT

        # Position Update
        # move particle based on its velocity

        self.x += self.vx * DT
        self.y += self.vy * DT
        return True

    def draw(self, screen):
        # Draw the particle as a small circle
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )

class BlackHole:
    def __init__(self, x, y, radius):
        # Position of the black hole
        self.x = x
        self.y = y

        # Radius = event horizon
        self.radius = radius

        # Black color
        self.color = (0, 0, 0)

    def draw(self, screen):
        # Draw the black hole as a black circle
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )

pygame.init()

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Simulation")

# Clock is used to control FPS
clock = pygame.time.Clock()


blackhole = BlackHole(
    CENTERPOINT[0],
    CENTERPOINT[1],
    radius=30
)

particles = []

for _ in range(NUM_PARTICLE):
    # Random angle around the black hole
    angle = random.uniform(0, 2 * math.pi)

    # Random distance from center
    distance = random.uniform(100, 400)

    # Convert polar coordinates to cartesian
    x = CENTERPOINT[0] + math.cos(angle) * distance
    y = CENTERPOINT[1] + math.sin(angle) * distance

    # Orbital speed formula (simplified physics)
    speed = math.sqrt(G / distance) * 0.001

    # Velocity must be perpendicular to radius for orbit
    vx = -math.sin(angle) * speed
    vy =  math.cos(angle) * speed

    particles.append(Particle(x, y, vx, vy))


running = True
while running:
    # Limit to 60 frames per second
    clock.tick(60)

    # Dark space background
    screen.fill((10, 10, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_particles = []
    for p in particles:
        alive = p.update(blackhole)
        if alive:
            new_particles.append(p)

    particles = new_particles

    blackhole.draw(screen)

    for p in particles:
        p.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
