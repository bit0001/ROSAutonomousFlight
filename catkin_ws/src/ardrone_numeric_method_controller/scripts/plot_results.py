#!/usr/bin/python3
"""
This is a script for plotting the results after following a trajectory.
"""
import matplotlib.pyplot as plt
from references import x_ref_n
from references import y_ref_n
from references import z_ref_n
from position import x_n
from position import y_n
from position import z_n
from errors import x_error
from errors import y_error
from errors import z_error


def show_legend(figure):
    legend = figure.legend(loc="best", shadow=True)

    for label in legend.get_texts():
        label.set_fontsize("medium")

    for label in legend.get_lines():
        label.set_linewidth(1.0)


def plot_reference_and_position(figure, reference, position, time):
    figure.plot(time, position, "b", label="Actual")
    figure.plot(time, reference, "r--", label="Reference")


def add_title_and_axis_labels(figure, title, x_label, y_label):
    figure.set_title(title)
    figure.set_xlabel(x_label)
    figure.set_ylabel(y_label)


def plot_errors(figure, error, time):
    zeros = [0 for e in range(len(error))]
    figure.plot(time, error, "b")
    figure.plot(time, zeros, "r--")


t_n = [0.1 * i for i in range(len(x_ref_n))]

whole_figure, plot_array = plt.subplots(2, 3)
whole_figure.suptitle("References, Positions and Errors", fontsize=16)

plot_reference_and_position(plot_array[0, 0], x_ref_n, x_n, t_n)
add_title_and_axis_labels(plot_array[0, 0], "X-position vs. time", "Time [s]", "X-position [m]")
show_legend(plot_array[0, 0])

plot_reference_and_position(plot_array[0, 1], y_ref_n, y_n, t_n)
add_title_and_axis_labels(plot_array[0, 1], "Y-position vs. time", "Time [s]", "Y-position [m]")
show_legend(plot_array[0, 1])

plot_reference_and_position(plot_array[0, 2], z_ref_n, z_n, t_n)
add_title_and_axis_labels(plot_array[0, 2], "Z-Position vs. time", "Time [s]", "Z-position [m]")
show_legend(plot_array[0, 2])

plot_errors(plot_array[1, 0], x_error, t_n)
add_title_and_axis_labels(plot_array[1, 0], "X-errors vs. time", "Time [s]", "X-Error %")

plot_errors(plot_array[1, 1], y_error, t_n)
add_title_and_axis_labels(plot_array[1, 1], "Y-errors vs. time", "Time [s]", "Y-Error %")

plot_errors(plot_array[1, 2], z_error, t_n)
add_title_and_axis_labels(plot_array[1, 2], "Z-errors vs. time", "Time [s]", "Z-Error %")

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
