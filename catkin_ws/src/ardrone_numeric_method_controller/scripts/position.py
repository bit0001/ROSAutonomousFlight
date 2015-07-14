#!/usr/bin/python3

"""This module contains the positions that have been generated after the drone has followed a trajectory."""

from util import get_float_list_from_txt_file
from constants import PATH_TO_POSITIONS_AND_TIME

x_n = get_float_list_from_txt_file(PATH_TO_POSITIONS_AND_TIME + "x_n")
y_n = get_float_list_from_txt_file(PATH_TO_POSITIONS_AND_TIME + "y_n")
z_n = get_float_list_from_txt_file(PATH_TO_POSITIONS_AND_TIME + "z_n")
