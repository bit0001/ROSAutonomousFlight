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

t_n = []

for i in range(len(x_ref_n)):
    t_n.append(0.1 * i)

figure, plot_array = plt.subplots(2, 3)
figure.suptitle("References, Positions and Errors", fontsize=16)

plot_array[0, 0].plot(t_n, x_n, 'b', label="Actual")
plot_array[0, 0].plot(t_n, x_ref_n, 'r--', label="Reference")
plot_array[0, 0].set_title('X-position vs. time')
plot_array[0, 0].set_xlabel("Time [s]")
plot_array[0, 0].set_ylabel("X-position [m]")
legend = plot_array[0, 0].legend(loc="best", shadow=True)

for label in legend.get_texts():
    label.set_fontsize('medium')

for label in legend.get_lines():
    label.set_linewidth(1.0)


plot_array[0, 1].plot(t_n, y_n, 'b', t_n, y_ref_n, 'r--')
plot_array[0, 1].set_title('Y-position vs. time')
plot_array[0, 1].set_xlabel("Time [s]")
plot_array[0, 1].set_ylabel("Y-position [m]")

plot_array[0, 2].plot(t_n, z_n, 'b', t_n, z_ref_n, 'r--')
plot_array[0, 2].set_title('Z-Position vs. time')
plot_array[0, 2].set_xlabel("Time [s]")
plot_array[0, 2].set_ylabel("Z-position [m]")

plot_array[1, 0].plot(t_n, x_error, 'r--')
plot_array[1, 0].set_title('X-errors vs. time')
plot_array[1, 0].set_xlabel("Time [s]")
plot_array[1, 0].set_ylabel("Error %")

plot_array[1, 1].plot(t_n, y_error, 'r--')
plot_array[1, 1].set_title('Y-errors vs. time')
plot_array[1, 1].set_xlabel("Time [s]")
plot_array[1, 1].set_ylabel("Error %")

plot_array[1, 2].plot(t_n, z_error, 'r--')
plot_array[1, 2].set_title('Z-errors vs. time')
plot_array[1, 2].set_xlabel("Time [s]")
plot_array[1, 2].set_ylabel("Error %")

plt.show()
