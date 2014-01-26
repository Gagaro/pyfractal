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
        c_real = real
        c_imaginary = imaginary
        for i in range(self.iterations):
            if pow(real, 2) + pow(imaginary, 2) > 4:
                return i
            tmp_imaginary = imaginary
            imaginary = 2 * real * imaginary + c_imaginary
            real = real * real - tmp_imaginary * tmp_imaginary + c_real
        return self.iterations
