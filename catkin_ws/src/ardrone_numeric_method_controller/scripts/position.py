#!/usr/bin/env python

"""This module contains functions to work with position data."""

from util import save_array_into_file
from constants import PATH_TO_POSITIONS_AND_TIME


def save_position_into_txt(position, txt_file_name):
    save_array_into_file(position, PATH_TO_POSITIONS_AND_TIME + txt_file_name + '.txt')
