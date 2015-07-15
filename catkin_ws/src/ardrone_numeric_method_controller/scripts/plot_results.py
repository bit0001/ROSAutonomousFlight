#!/usr/bin/python3
"""
This is a script for plotting the results after following a trajectory.
"""
import matplotlib.pyplot as plt
from util import plot_reference_and_position, add_title_and_axis_labels, show_legend, plot_errors
from references import x_ref_n, y_ref_n, z_ref_n
from position import x_n, y_n, z_n
from errors import x_error, y_error, z_error

t_n = [0.1 * i for i in range(len(x_ref_n))]

whole_figure, plot_array = plt.subplots(2, 3)
whole_figure.suptitle("References, Positions and Errors", fontsize=16, fontweight='bold')

plot_reference_and_position(plot_array[0, 0], x_ref_n, x_n, t_n)
add_title_and_axis_labels(plot_array[0, 0], "X-position vs. time", "Time [s]", "X-position [m]")
show_legend(plot_array[0, 0])
plot_array[0, 0].grid()

plot_reference_and_position(plot_array[0, 1], y_ref_n, y_n, t_n)
add_title_and_axis_labels(plot_array[0, 1], "Y-position vs. time", "Time [s]", "Y-position [m]")
show_legend(plot_array[0, 1])
plot_array[0, 1].grid()

plot_reference_and_position(plot_array[0, 2], z_ref_n, z_n, t_n)
add_title_and_axis_labels(plot_array[0, 2], "Z-Position vs. time", "Time [s]", "Z-position [m]")
show_legend(plot_array[0, 2])
plot_array[0, 2].grid()

plot_errors(plot_array[1, 0], x_error, t_n)
add_title_and_axis_labels(plot_array[1, 0], "X-error vs. time", "Time [s]", "X-Error")
plot_array[1, 0].grid()

plot_errors(plot_array[1, 1], y_error, t_n)
add_title_and_axis_labels(plot_array[1, 1], "Y-error vs. time", "Time [s]", "Y-Error %")
plot_array[1, 1].grid()

plot_errors(plot_array[1, 2], z_error, t_n)
add_title_and_axis_labels(plot_array[1, 2], "Z-error vs. time", "Time [s]", "Z-Error %")
plot_array[1, 2].grid()

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
