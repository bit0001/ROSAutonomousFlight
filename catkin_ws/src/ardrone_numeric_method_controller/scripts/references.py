#!/usr/bin/env python

"""
This is module contains the references that will be loaded from txt files. These txt files have been generated
either by defining a trajectory in MATLAB or bye drawing a trajectory in the mobile app.
"""

from util import *
from constants import PATH_TO_REFERENCES


def string_array_to_number_array(string_array):
    number_array = []
    for item in string_array:
        number_array.append(float(item))

    return number_array


x_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "x_ref_n.txt"))
y_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "y_ref_n.txt"))
z_ref_n = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "z_ref_n.txt"))
x_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "x_ref_np1.txt"))
y_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "y_ref_np1.txt"))
z_ref_np1 = string_array_to_number_array(get_array_from_file(PATH_TO_REFERENCES + "z_ref_np1.txt"))
