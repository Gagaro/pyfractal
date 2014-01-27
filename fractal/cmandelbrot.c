#include "Python.h"

static PyObject *
mandelbrot(PyObject *self, PyObject *args)
{
  int iterations,
    i;
  double c_real,
    c_imaginary,
    real,
    imaginary,
    tmp;

  if (!PyArg_ParseTuple(args, "ddi", &c_real, &c_imaginary, &iterations))
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

static PyMethodDef Methods[] = {
      {"mandelbrot",  mandelbrot, METH_VARARGS,
       "Calculate number of iterations for a given complex."},
      {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initcmandelbrot(void)
{
  (void) Py_InitModule("cmandelbrot", Methods);
}
