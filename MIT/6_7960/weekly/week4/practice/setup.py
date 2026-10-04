import numpy as np
from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("main.pyx", compiler_directives={"language_level": "3"}),
    include_dirs=[
        np.get_include()
    ],  # Included if you want to swap to NumPy arrays later
)
