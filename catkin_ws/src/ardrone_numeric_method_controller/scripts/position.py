#!/usr/bin/env python

"""This module contains functions to work with position data."""

from util import save_array_into_file
from constants import PATH_TO_POSITIONS_AND_TIME

t_n = []
x_n = []
y_n = []
z_n = []
psi_n = []
psi_ez_n = []

def save_position_into_txt(position, txt_file_name):
    save_array_into_file(position, PATH_TO_POSITIONS_AND_TIME + txt_file_name + '.txt')
