"""This module contains functions to work with position data."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

from util import save_array_into_file

PATH_TO_POSITIONS_AND_TIME = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                             "ardrone_numeric_method_controller/scripts/positionsAndTime/"

def save_position_into_txt(position, txt_file_name):
    save_array_into_file(position, PATH_TO_POSITIONS_AND_TIME + txt_file_name + '.txt')
