#setup.py
from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(ext_modules = cythonize('second_analyze_plot_combination.pyx'), include_dirs=[np.get_include()])