#!/usr/bin/env python

"""This is the main module of the project where the algorithm is executed."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi", "Sika Abarca", "Gustavo Scaglia", "Andres Rosales"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

import math
from references import *
from position import *
from constants import *
from controller import *

controller = ARDroneController()

def save_positions():
    save_list_into_txt(x_n, "x_n")
    save_list_into_txt(y_n, "y_n")
    save_list_into_txt(z_n, "z_n")


def follow_trajectory():
    sampling_frequency = rospy.Rate(1 / T0)
    for i in range(len(x_ref_n)):
        if controller.last_time is None:
            controller.last_time = rospy.Time.now()
            dt = 0
        else:
            current_time = rospy.Time.now()
            dt = (current_time - controller.last_time)
            controller.last_time = current_time

        t_n.append(i * T0)
        dx = dt * controller.required_navigation_data["vx"]
        dy = dt * controller.required_navigation_data["vy"]

        try:
            x_n.append(x_n[-1] + dx)
            y_n.append(y_n[-1] + dy)
        except IndexError:
            x_n.append(dx)
            y_n.append(dy)

        z_n.append(controller.required_navigation_data["z"])
        psi_n.append(controller.required_navigation_data["psi"])

        psi_ez_n.append(math.atan2(y_ref_np1[i] - K_V_XY * (y_ref_n[i] - y_n[-1]) - y_n[-1],
                                   x_ref_np1[i] - K_V_XY * (x_ref_n[i] - x_n[-1]) - x_n[-1]))

        v_xy = (1 / T0) * ((x_ref_n[i] - K_V_XY * (x_ref_n[i] - x_n[-1]) - x_n[-1]) * math.cos(psi_ez_n[-1]) +
                           (y_ref_np1[i] - K_V_XY * (y_ref_n[i] - y_n[-1]) - y_n[-1]) * math.sin(psi_ez_n[-1]))

        v_z = (1 / T0) * (z_ref_n[i] - K_V_Z * (z_ref_n[i] - z_n[-1]) - z_n[-1])

        try:
            omega_psi = (1 / T0) * (psi_ez_n[-1] - K_OMEGA_PSI * (psi_ez_n[-2] - psi_n[-2]) - psi_n[-2])
        except IndexError:
            omega_psi = (1 / T0) * (psi_ez_n[-1])

        controller.send_linear_and_angular_velocities([v_xy / V_XY_MAX, 0, v_z / V_Z_MAX],
                                                      [0, 0, omega_psi / OMEGA_PSI_MAX])
        sampling_frequency.sleep()

if __name__ == "__main__":
    rospy.init_node("controller_node", anonymous=True)

    rospy.sleep(1)
    print("Ready!")
    controller.send_flat_trim()

    controller.send_take_off()
    rospy.sleep(7.0)
    print("Start")

    follow_trajectory()
    controller.send_land()

    save_positions()

    print("done!")
