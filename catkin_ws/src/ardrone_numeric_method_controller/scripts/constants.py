#!/usr/bin/env python

"""This module contains relevant constants for the project"""


from util import get_list_from_file

PATH_TO_SCRIPTS = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                  "ardrone_numeric_method_controller/scripts/"
PATH_TO_POSITIONS_AND_TIME = PATH_TO_SCRIPTS + "positionsAndTime/"
PATH_TO_REFERENCES = PATH_TO_SCRIPTS + "referenceAndConstantFiles/"

T0 = 0.1
TP = 2 * T0
K_V_XY = get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[0]
K_V_Z = get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[1]
K_OMEGA_PSI = get_list_from_file(PATH_TO_REFERENCES + "control_constants.txt")[2]
V_XY_MAX = 2.0
V_Z_MAX = 2.0
OMEGA_PSI_MAX = 1.75
