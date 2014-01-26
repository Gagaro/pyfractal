#include "Python.h"

static PyObject *
mandelbrot(PyObject *self, PyObject *args)
{
  int c_real,
    c_imaginary,
    iterations,
    i,
    real,
    imaginary,
    tmp;

  if (!PyArg_ParseTuple(args, "iii", &c_real, &c_imaginary, &iterations))
    return NULL;
  real = c_real;
  imaginary = c_imaginary;
  for (i = 0 ; i < iterations ; i++)
    {
      if (real * real + imaginary * imaginary > 4)
	break;
      tmp = imaginary;
      imaginary = 2 * real * imaginary + c_imaginary;
      real = real * real - tmp * tmp + c_real;
    }
  return Py_BuildValue("i", i);
}
