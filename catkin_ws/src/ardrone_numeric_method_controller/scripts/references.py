#!/usr/bin/env python

"""
This is module contains the references that will be loaded from txt files. These txt files have been generated
either by defining a trajectory in MATLAB or bye drawing a trajectory in the mobile app.
"""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"



from util import *

PATH_TO_REFERENCES = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/ardrone_numeric_method_controller/" \
                     "scripts/referenceAndConstantFiles/"

def string_array_to_number_array(string_array):
    number_array = []
    for i in string_array:
        number_array.append(float(i))

    return number_array

x_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'x_ref_n.txt'))
y_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'y_ref_n.txt'))
z_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'z_ref_n.txt'))
x_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'x_ref_np1.txt'))
y_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'y_ref_np1.txt'))
z_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + 'z_ref_np1.txt'))
