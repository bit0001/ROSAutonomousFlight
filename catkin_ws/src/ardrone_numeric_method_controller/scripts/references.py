#!/usr/bin/env python

"""
This is module contains the references that will be loaded from txt files. These txt files have been generated
either by defining a trajectory in MATLAB or bye drawing a trajectory in the mobile app.
"""

from util import *
from constants import HOST
from constants import EMAIL
from constants import PASSWORD
from constants import PATH_TO_REFERENCES


def string_list_to_float_list(string_array):
    float_list = []
    for item in string_array:
        float_list.append(float(item))

    return float_list

save_attached_files_from_email(HOST, EMAIL, PASSWORD, PATH_TO_REFERENCES)

x_ref_n = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "x_ref_n.txt"))
y_ref_n = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "y_ref_n.txt"))
z_ref_n = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "z_ref_n.txt"))
x_ref_np1 = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "x_ref_np1.txt"))
y_ref_np1 = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "y_ref_np1.txt"))
z_ref_np1 = string_list_to_float_list(get_list_from_file(PATH_TO_REFERENCES + "z_ref_np1.txt"))
