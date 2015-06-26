#!/usr/bin/env python

"""This module contains controllers which hold the necessary functions to control an AR.Drone."""

import rospy
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3
import std_srvs.srv
import math

QUEUE_SIZE = 10

def adjust_psi(initial_psi, read_psi):
    adjusted_psi = read_psi - initial_psi

    if adjusted_psi < -180:
        adjusted_psi += 360
    elif adjusted_psi > 180:
        adjusted_psi -= 360

    return adjusted_psi

class ARDroneController:
    def __init__(self):
        self.navigation_data = rospy.Subscriber("/ardrone/navdata", Navdata, self.callback_navigation_data)
        self.required_navigation_data = {'vx': None, 'vy': None, 'z': None, 'psi': None}
        self.last_time = None
        self.initial_psi = None

        self.pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty, queue_size=QUEUE_SIZE)
        self.pub_land = rospy.Publisher("/ardrone/land", Empty, queue_size=QUEUE_SIZE)
        self.pub_reset = rospy.Publisher("/ardrone/reset", Empty, queue_size=QUEUE_SIZE)
        self.pub_velocity = rospy.Publisher("/cmd_vel", Twist, queue_size=QUEUE_SIZE)

    def callback_navigation_data(self, data):
        self.required_navigation_data["vx"] = data.vx / 1e3
        self.required_navigation_data["vy"] = data.vy / 1e3
        self.required_navigation_data["z"] = data.altd / 1e3

        if self.initial_psi is None:
            self.required_navigation_data["psi"] = math.radians(data.rotZ)
        else:
            self.required_navigation_data["psi"] = math.radians(adjust_psi(self.initial_psi, data.rotZ))

    def get_ready(self, n=1):
        rospy.sleep(n)
        print("Ready!")

    def send_take_off(self):
        print("Take off...")
        self.pub_takeoff.publish(Empty())

    def send_take_off_and_stabilize(self, n):
        self.send_take_off()
        self.initial_psi = self.required_navigation_data["psi"]
        rospy.sleep(n)

    def send_land(self):
        print('Land...')
        self.pub_land.publish(Empty())

    def send_reset(self):
        print("Reset...")
        self.pub_reset.publish(Empty())

    def send_flat_trim(self):
        print("Flat trim...")
        trim = rospy.ServiceProxy("/ardrone/flattrim", std_srvs.srv.Empty)
        trim()

    def send_linear_and_angular_velocities(self, linear_velocity, angular_velocity):
        self.pub_velocity.publish(Twist(
            Vector3(linear_velocity[0], linear_velocity[1], linear_velocity[2]),
            Vector3(angular_velocity[0], angular_velocity[1], angular_velocity[2])))


class ARDroneBasicController(ARDroneController):
    def move_forward(self, speed):
        self.send_linear_and_angular_velocities([speed, 0, 0], [0, 0, 0])

    def move_backward(self, speed):
        self.send_linear_and_angular_velocities([-speed, 0, 0], [0, 0, 0])

    def move_left(self, speed):
        self.send_linear_and_angular_velocities([0, speed, 0], [0, 0, 0])

    def move_right(self, speed):
        self.send_linear_and_angular_velocities([0, -speed, 0, 0], [0, 0, 0])

    def move_up(self, speed):
        self.send_linear_and_angular_velocities([0, 0, speed], [0, 0, 0])

    def move_down(self, speed):
        self.send_linear_and_angular_velocities([0, 0, -speed], [0, 0, 0])

    def move_clockwise(self, speed):
        self.send_linear_and_angular_velocities([0, 0, 0], [0, 0, speed])

    def move_counterclockwise(self, speed):
        self.send_linear_and_angular_velocities([0, 0, 0], [0, 0, -speed])

    def hover(self):
        self.send_linear_and_angular_velocities([0, 0, 0], [0, 0, 0])
