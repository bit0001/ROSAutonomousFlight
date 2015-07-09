#!/usr/bin/env python
# coding=utf-8

"""This is the main module of the project where the algorithm is executed."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi", "Sika Abarca", "Gustavo Scaglia", "Andrés Rosales"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

from references import *
from position import *
from constants import *
from controller import *

controller = ARDroneController()


def save_positions():
    save_list_into_txt(x_n, "x_n")
    save_list_into_txt(y_n, "y_n")
    save_list_into_txt(z_n, "z_n")
    save_list_into_txt(t_n, "t_n")
    save_list_into_txt(psi_n, "psi_n")


def print_useful_data(controller, iteration):
    data = controller.required_navigation_data
    print("Iteration: " + str(iteration))
    print("\tX speed: " + str(data["vx"]))
    print("\tY speed: " + str(data["vy"]))
    print("\tZ position: " + str(data["z"]))
    print("\tPsi: " + str(math.degrees(controller.required_navigation_data["psi"])))


def print_adjusted_control_actions(v_xy, v_z, omega_psi):
    print("Adjusted Control Actions:")
    print("\tV_XY: " + str(v_xy))
    print("\tV_Z: " + str(v_z))
    print("\tOMEGA_PSI: " + str(omega_psi))


def print_non_adjusted_control_actions(v_xy, v_z, omega_psi):
    print("Non-Adjusted Control Actions:")
    print("\tV_XY: " + str(v_xy))
    print("\tV_Z: " + str(v_z))
    print("\tOMEGA_PSI: " + str(omega_psi))


def follow_trajectory():
    sampling_frequency = rospy.Rate(1 / T0)
    for i in range(len(x_ref_n)):
        if controller.last_time is None:
            controller.last_time = rospy.Time.now()
            dt = 0
        else:
            current_time = rospy.Time.now()
            dt = (current_time - controller.last_time).to_sec()
            controller.last_time = current_time

        t_n.append(i * T0)
        current_psi = controller.required_navigation_data["psi"]

        dx_local = dt * controller.required_navigation_data["vx"]
        dy_local = dt * controller.required_navigation_data["vy"]

        try:
            dx_global = dx_local * math.cos(psi_n[-1]) - dy_local * math.sin(psi_n[-1])
            dy_global = dx_local * math.sin(psi_n[-1]) + dy_local * math.cos(psi_n[-1])
        except IndexError:
            dx_global = dx_local * math.cos(current_psi) - dy_local * math.sin(current_psi)
            dy_global = dx_local * math.sin(current_psi) + dy_local * math.cos(current_psi)

        try:
            x_n.append(x_n[-1] + dx_global)
            y_n.append(y_n[-1] + dy_global)
        except IndexError:
            x_n.append(dx_global)
            y_n.append(dy_global)

        z_n.append(controller.required_navigation_data["z"])
        psi_n.append(current_psi)

        x_control_action = compute_control_action(x_ref_np1[i], x_ref_n[i], x_n[-1], K_V_X)
        y_control_action = compute_control_action(y_ref_np1[i], y_ref_n[i], y_n[-1], K_V_Y)

        v_x = (1 / T0) * (x_control_action * math.cos(psi_n[-1]) + y_control_action * math.sin(psi_n[-1]))
        v_y = (1 / T0) * (-x_control_action * math.sin(psi_n[-1]) + y_control_action * math.cos(psi_n[-1]))
        v_z = (1 / T0) * compute_control_action(z_ref_np1[i], z_ref_n[i], z_n[-1], K_V_Z)

        v_x_adjusted = adjust_control_action(v_x / V_X_MAX)
        v_y_adjusted = adjust_control_action(v_y / V_Y_MAX)
        v_z_adjusted = adjust_control_action(v_z / V_Z_MAX)

        controller.send_linear_and_angular_velocities([v_x_adjusted, v_y_adjusted, v_z_adjusted], [0, 0, 0])
        sampling_frequency.sleep()

if __name__ == "__main__":
    rospy.init_node("controller_node", anonymous=True)

    controller.get_ready()
    controller.send_reset()
    controller.send_flat_trim()
    controller.send_take_off_and_stabilize(7.0)
    print("Start")
    follow_trajectory()
    controller.send_land()
    save_positions()
    print("Done!")
