import pygame

from fractal import mandelbrot

WIDTH = 300
HEIGHT = 300

pygame.init()
pygame.font.init()


class Screen(object):
    def __init__(self, width, height, fractal, caption="Mandelbrot"):
        self.width = width
        self.height = height
        self.click = None
        self.fractal = fractal
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont('monospace', 15)
        pygame.display.set_caption(caption)

    def set_click(self, click):
        self.click = click

    def draw_fractal(self):
        self.fractal_surface = pygame.Surface((self.width, self.height))
        # main loop calculating the Mandelbrot Set
        for x in range(self.width):
            for y in range(self.height):
                color = self.fractal.get(x, y) * 255 / mandelbrot.ITERATIONS
                self.fractal_surface.set_at((x, y), (color, color, color))
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (0, 0, x, self.height))
            pygame.display.flip()
        self.screen.blit(self.fractal_surface, (0, 0))
        pygame.display.flip()

    def draw_rect(self, pos1, pos2):
        x = min(pos1[0], pos2[0])
        y = min(pos1[1], pos2[1])
        width = abs(pos1[0] - pos2[0])
        height = abs(pos1[1] - pos2[1])
        pygame.draw.rect(self.screen, (0, 255, 0), (x, y, width, height), 1)

    def draw_position(self, pos):
        c_r, c_i = self.fractal.get_c(*(pos))
        label = self.font.render("%f + %fi" % (c_r, c_i), 1, (255, 0, 0))
        self.screen.blit(self.fractal_surface, (0, 0))
        if self.click is not None:
            self.draw_rect(self.click, pos)
        self.screen.blit(label, (10, 10))


def application(width, height, min_r=-2.0, max_r=1.0, min_i=-1.5):
    fractal = mandelbrot.Mandelbrot(width, height, min_r, max_r, min_i)
    screen = Screen(width, height, fractal)
    screen.draw_fractal()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                screen.draw_position(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen.set_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = screen.click
                    min_x = min(click[0], event.pos[0])
                    max_x = max(click[0], event.pos[0])
                    min_y = min(click[1], event.pos[1])
                    max_y = max(click[1], event.pos[1])
                    c1 = fractal.get_c(min_x, min_y)
                    c2 = fractal.get_c(max_x, max_y)
                    # @TODO
                    screen.set_click(None)
            pygame.display.flip()


def main():
    application(WIDTH, HEIGHT)

main()
