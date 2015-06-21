#!/usr/bin/env python

"""This is the main module of the project where the algorithm is executed."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi", "Sika Abarca", "Gustavo Scaglia", "Andres Rosales"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

from references import *
from position import save_position_into_txt
from constants import *

print("x_ref_n:\n", x_ref_n)
print("y_ref_n:\n", y_ref_n)
print('z_ref_n:\n', z_ref_n)
print('x_ref_np1:\n', x_ref_np1)
print('y_ref_np1:\n', y_ref_np1)
print('z_ref_np1:\n', z_ref_np1)

print('This is K_V_XY:', K_V_XY)
print('This is K_V_Z:', K_V_Z)
print('This is K_OMEGA_PSI:', K_OMEGA_PSI)

save_position_into_txt(x_ref_n, "x_n")
save_position_into_txt(y_ref_n, "y_n")
save_position_into_txt(z_ref_n, "z_n")
