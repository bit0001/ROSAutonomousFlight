#!/usr/bin/env python

"""This is the main module of the project where the algorithm is executed."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi Rob Knight", "Sika Abarca"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"


from util import *


PATH_TO_REFERENCES = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/ardrone_numeric_method_controller/" \
                     "scripts/referenceAndConstantFiles/"

get_array_from_file(PATH_TO_REFERENCES + 'x_ref_n.txt')
