#!/usr/bin/env python

"""
This is module contains the references that will be loaded from txt files. These txt files have been generated
either by defining a trajectory in MATLAB or bye drawing a trajectory in the mobile app.
"""

from util import get_float_list_from_txt_file
from util import *
from constants import PATH_TO_REFERENCES

x_ref_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "x_ref_n")
y_ref_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "y_ref_n")
z_ref_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "z_ref_n")
x_ref_np1 = get_float_list_from_txt_file(PATH_TO_REFERENCES + "x_ref_np1")
y_ref_np1 = get_float_list_from_txt_file(PATH_TO_REFERENCES + "y_ref_np1")
z_ref_np1 = get_float_list_from_txt_file(PATH_TO_REFERENCES + "z_ref_np1")
