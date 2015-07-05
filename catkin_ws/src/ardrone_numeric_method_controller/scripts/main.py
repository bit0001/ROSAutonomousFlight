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
    save_list_into_txt(psi_ez_n, "psi_ez_n")
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

        x_control_action = compute_control_action(x_ref_np1[i], x_ref_n[i], x_n[-1], K_V_XY)
        y_control_action = compute_control_action(y_ref_np1[i], y_ref_n[i], y_n[-1], K_V_XY)
        psi_ez_n.append(math.atan2(y_control_action, x_control_action))

        v_xy = (1 / T0) * (x_control_action * math.cos(psi_ez_n[-1]) + y_control_action * math.sin(psi_ez_n[-1]))
        v_xy_adjusted = adjust_control_action(v_xy / V_XY_MAX)
        v_z = (1 / T0) * compute_control_action(z_ref_np1[i], z_ref_n[i], z_n[-1], K_V_Z)
        v_z_adjusted = adjust_control_action(v_z / V_Z_MAX)

        try:
            omega_psi = (1 / T0) * (psi_ez_n[-1] - K_OMEGA_PSI * (psi_ez_n[-2] - psi_n[-2]) - psi_n[-2])
        except IndexError:
            omega_psi = (1 / T0) * (psi_ez_n[-1])

        omega_psi_adjusted = adjust_control_action(omega_psi / OMEGA_PSI_MAX)

        print_useful_data(controller, i)
        print_non_adjusted_control_actions(v_xy, v_z, omega_psi)
        print_adjusted_control_actions(v_xy_adjusted, v_z_adjusted, omega_psi_adjusted)

        controller.send_linear_and_angular_velocities([v_xy_adjusted, 0, v_z_adjusted],
                                                      [0, 0, omega_psi_adjusted])
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
