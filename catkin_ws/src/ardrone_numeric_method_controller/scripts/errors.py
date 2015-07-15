#!/usr/bin/python3
"""
This module contains the percentage of errors that have been computed using the references and the positions generated
after a trajectory is completed.
"""

from numpy import array
from references import *
from position import *


def compute_percentage_error(approximate_list, exact_list):
    return 100.0 * abs((array(approximate_list) - array(exact_list)) / array(exact_list))


x_error = compute_percentage_error(x_n, x_ref_n)
y_error = compute_percentage_error(y_n, y_ref_n)
z_error = compute_percentage_error(z_n, z_ref_n)
