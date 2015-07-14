#!/usr/bin/python3
"""
This is a script for plotting the results after following a trajectory.
"""
import numpy as np
import matplotlib.pyplot as plt
from references import x_ref_n
from references import y_ref_n
from references import z_ref_n
from references import get_float_list_from_txt_file
from references import PATH_TO_REFERENCES

x_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "x_ref_n")
y_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "y_ref_n")
z_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "z_ref_n")
t_n = get_float_list_from_txt_file(PATH_TO_REFERENCES + "x_ref_n")
t_n = []

for i in range(len(x_ref_n)):
    t_n.append(0.1 * i)

figure, plot_array = plt.subplots(2, 3)
plot_array[0, 0].plot(t_n, x_ref_n, 'r--', t_n, x_n, 'bs')
plot_array[0, 0].set_title('X-position vs. time')
plot_array[0, 1].plot(t_n, y_ref_n, 'r--', t_n, y_n, 'bs')
plot_array[0, 1].set_title('Y-position vs. time')
plot_array[0, 2].plot(t_n, z_ref_n, 'r--', t_n, z_n, 'bs')
plot_array[0, 2].set_title('Z-Position vs. time')
plot_array[1, 0].set_title('X-errors vs. time')
plot_array[1, 1].set_title('Y-errors vs. time')
plot_array[1, 2].set_title('Z-errors vs. time')
plt.show()
