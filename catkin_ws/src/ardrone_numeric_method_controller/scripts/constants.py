#!/usr/bin/python3
"""This module contains relevant constants for the project"""


from util import get_list_from_file

PATH_TO_SCRIPTS = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                  "ardrone_numeric_method_controller/scripts/"
PATH_TO_POSITIONS_AND_TIME = PATH_TO_SCRIPTS + "positionsAndTime/"
PATH_TO_REFERENCES = PATH_TO_SCRIPTS + "referenceAndConstantFiles/"


T0 = 0.1
TP = 2 * T0
K_V_X = eval(get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[0])
K_V_Y = eval(get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[1])
K_V_Z = eval(get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[2])
V_X_MAX = 4.0
V_Y_MAX = 4.0
V_Z_MAX = 1.0
