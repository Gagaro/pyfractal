import logging

try:
    import cmandelbrot
    CMANDELBROT = True
except ImportError:
    CMANDELBROT = False
    logging.warning("cmandelbrot not present, using python implementation.")

ITERATIONS = 300


class Mandelbrot(object):
    def __init__(self, width, height, min_r=-2.0, max_r=1.0, min_i=-1.5,
                 iterations=ITERATIONS):
        self.min_r = min_r
        self.max_r = max_r
        self.min_i = min_i
        self.max_i = min_i + (max_r - min_r) * height / width
        self.width = width
        self.height = height
        self.iterations=iterations
        self.pre_height = (self.max_r - self.min_r) / (self.width - 1)
        self.pre_width = (self.max_i - self.min_i) / (self.height - 1)

    def get_c(self, x, y):
        real = self.min_r + x * self.pre_height
        imaginary = self.min_i + y * self.pre_width
        return (real, imaginary)

    def get(self, x, y):
        return self.mandelbrot(*(self.get_c(x, y)))

    def mandelbrot(self, real, imaginary):
        if CMANDELBROT:
            return cmandelbrot.mandelbrot(real, imaginary, self.iterations)
        c = complex(real, imaginary)
        z = c
        for i in xrange(self.iterations):
            if abs(z) > 2:
                return i
            z = z * z + c
        return self.iterations
