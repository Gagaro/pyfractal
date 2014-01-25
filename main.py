import pygame

from fractal import mandelbrot


width = 300
height = 300

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('monospace', 15)
pygame.display.set_caption('Mandelbrot')


fractal_surface = pygame.Surface((width, height))
fractal = mandelbrot.Mandelbrot(width, height)

# main loop calculating the Mandelbrot Set
for x in range(width):
    for y in range(height):
        color = fractal.get(x, y) * 255 / mandelbrot.ITERATIONS
        fractal_surface.set_at((x, y), (color, color, color))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, x, height))
    pygame.display.flip()

screen.blit(fractal_surface, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            c_r, c_i = fractal.get_c(*(event.pos))
            label = font.render("%d / %d" % (c_r, c_i), 1, (255, 0, 0))
            screen.blit(label, (10, 10))
        pygame.display.flip()
