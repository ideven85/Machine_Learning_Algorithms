from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [Extension("main", ["main.pyx"])]

setup(ext_modules=cythonize(extensions))
