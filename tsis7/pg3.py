import pygame

pygame.init()


# to display graphics - you need to create a window
HEIGHT, WIDTH = 1400, 700
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('hodilka brodilka')
radius = 25
x, y = 25, 25
step = 10
dx, dy = 0, 0
clock = pygame.time.Clock()


running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red, green, blue; ( 0 - 255 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > radius:
        dx = 0
        dy = -1
    elif pressed[pygame.K_DOWN] and y < WIDTH - radius:
        dx = 0
        dy = 1
    elif pressed[pygame.K_LEFT] and x > radius:
        dx = -1
        dy = 0
    elif pressed[pygame.K_RIGHT] and x < HEIGHT - radius:
        dx = 1
        dy = 0
    else:
        dx, dy = 0, 0
    x = x + dx * step
    y = y + dy * step

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius=radius)
    pygame.display.flip()
    clock.tick(100)