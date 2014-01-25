import pygame

from fractal import mandelbrot

width = 300
height = 300


def init():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('monospace', 15)
    pygame.display.set_caption('Mandelbrot')
    return (screen, font)


def draw_fractal(screen, fractal):
    fractal_surface = pygame.Surface((width, height))
    # main loop calculating the Mandelbrot Set
    for x in range(width):
        for y in range(height):
            color = fractal.get(x, y) * 255 / mandelbrot.ITERATIONS
            fractal_surface.set_at((x, y), (color, color, color))
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, x, height))
        pygame.display.flip()
    screen.blit(fractal_surface, (0, 0))
    pygame.display.flip()
    return fractal_surface


def draw_rect(screen, pos1, pos2):
    x = min(pos1[0], pos2[0])
    y = min(pos1[1], pos2[1])
    width = abs(pos1[0] - pos2[0])
    height = abs(pos1[1] - pos2[1])
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height), 1)


def main():
    screen, font = init()
    fractal = mandelbrot.Mandelbrot(width, height)
    fractal_surface = draw_fractal(screen, fractal)
    click = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                c_r, c_i = fractal.get_c(*(event.pos))
                label = font.render("%f + %fi" % (c_r, c_i), 1, (255, 0, 0))
                screen.blit(fractal_surface, (0, 0))
                if click is not None:
                    draw_rect(screen, click, event.pos)
                screen.blit(label, (10, 10))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    min_x = min(click[0], event.pos[0])
                    max_x = max(click[0], event.pos[0])
                    min_y = min(click[1], event.pos[1])
                    max_y = max(click[1], event.pos[1])
                    c1 = fractal.get_c(min_x, min_y)
                    c2 = fractal.get_c(max_x, max_y)
                    fractal = mandelbrot.Mandelbrot(width, height,
                                                    min_r=c1[0], max_r=c2[0],
                                                    min_i=c1[1])
                    fractal_surface = draw_fractal(screen, fractal)
                    click = None
            pygame.display.flip()


main()
