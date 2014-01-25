from math import sqrt

ITERATIONS = 300


class Mandelbrot(object):
    def __init__(self, width, height, min_x=-2.0, max_x=1.0, min_y=-1.5,
                 iterations=ITERATIONS):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = min_y + (max_x - min_x) * height / width
        self.width = width
        self.height = height
        self.iterations=iterations

        self.pre_height = (self.max_x - self.min_x) / (self.width - 1)
        self.pre_width = (self.max_y - self.min_y) / (self.height - 1)

    def get_c(self, x, y):
        real = self.min_x + x * self.pre_height
        imaginary = self.max_y - y * self.pre_width
        return (real, imaginary)

    def get(self, x, y):
        return self.mandelbrot(*(self.get_c(x, y)))

    def mandelbrot(self, real, imaginary):
        c_real = real
        c_imaginary = imaginary
        for i in range(self.iterations):
            if pow(real, 2) + pow(imaginary, 2) > 4:
                return i
            tmp_imaginary = imaginary
            imaginary = 2 * real * imaginary + c_imaginary
            real = real * real - tmp_imaginary * tmp_imaginary + c_real
        return self.iterations
