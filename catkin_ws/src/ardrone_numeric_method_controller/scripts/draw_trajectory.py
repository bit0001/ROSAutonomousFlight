#!/usr/bin/python3
"""
This is a script for plotting the trajectory that the drone is supposed to follow.
"""
import matplotlib.pyplot as plt
from util import add_title_and_axis_labels
from references import x_ref_n, y_ref_n, z_ref_n
from references import x_ref_np1, y_ref_np1, z_ref_np1

t_n = [0.1 * i for i in range(len(x_ref_n))]
t_np1 = t_n[1:] + [t_n[-1]]

whole_figure, plot_array = plt.subplots(2, 2)
whole_figure.set_size_inches(15.5, 12.5, forward=True)
whole_figure.suptitle("References at n and at n+1", fontsize=16)

plot_array[0, 0].plot(x_ref_n, y_ref_n)
add_title_and_axis_labels(plot_array[0, 0], "XY reference trajectory at n", "X-position in [m]", "Y-position in [m]")
plot_array[0, 1].plot(t_n, z_ref_n)
add_title_and_axis_labels(plot_array[0, 1], "Z reference vs t at n", "Z reference position in [m]", "Time in [s]")
plot_array[1, 0].plot(x_ref_np1, y_ref_np1)
add_title_and_axis_labels(plot_array[1, 0], "XY reference trajectory at n+1", "X-position in [m]", "Y-position in [m]")
plot_array[1, 1].plot(t_np1, z_ref_np1)
add_title_and_axis_labels(plot_array[1, 1], "Z reference vs t at n+1", "Z reference position in [m]", "Time in [s]")

plt.show()