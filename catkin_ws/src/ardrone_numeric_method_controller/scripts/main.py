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
from util import *

PATH_TO_POSITIONS_AND_TIME = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                             "ardrone_numeric_method_controller/scripts/positionsAndTime/"

print("x_ref_n:\n", x_ref_n)
print("y_ref_n:\n", y_ref_n)
print('z_ref_n:\n', z_ref_n)
print('x_ref_np1:\n', x_ref_np1)
print('y_ref_np1:\n', y_ref_np1)
print('z_ref_np1:\n', z_ref_np1)

save_array_into_file(x_ref_n, PATH_TO_POSITIONS_AND_TIME + 'x_n.txt')
save_array_into_file(y_ref_n, PATH_TO_POSITIONS_AND_TIME + 'y_n.txt')
save_array_into_file(z_ref_n, PATH_TO_POSITIONS_AND_TIME + 'z_n.txt')
