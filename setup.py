from distutils.core import setup, Extension


mandelbrot = Extension('cmandelbrot',
                       sources = ['fractal/cmandelbrot.c'])

setup(
    name = 'PyFractal',
    version = '0.1',
    description = 'Build c extension for optimizing fractals rendering.',
    ext_modules = [mandelbrot]
    )
