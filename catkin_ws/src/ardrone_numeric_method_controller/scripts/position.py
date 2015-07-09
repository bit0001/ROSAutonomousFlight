#!/usr/bin/env python

"""This module contains functions to work with position data."""

from util import save_list_into_file
from constants import PATH_TO_POSITIONS_AND_TIME

t_n = []
x_n = []
y_n = []
z_n = []
psi_n = []

def save_list_into_txt(a_list, txt_file_name):
    save_list_into_file(a_list, PATH_TO_POSITIONS_AND_TIME + txt_file_name + '.txt')
