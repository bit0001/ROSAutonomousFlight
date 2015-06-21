#!/usr/bin/env python

"""This module contains controllers which hold the necessary functions to control an AR.Drone."""

import rospy
from std_msgs.msg import Empty

QUEUE_SIZE = 10

class ARDroneController:
    def __init__(self):
        self.pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty, queue_size=QUEUE_SIZE)
        self.pub_land = rospy.Publisher("/ardrone/land", Empty, queue_size=QUEUE_SIZE)
        self.pub_reset = rospy.Publisher("/ardrone/reset", Empty, queue_size=QUEUE_SIZE)

    def send_take_off(self):
        print("Take off...")
        self.pub_takeoff.publish(Empty())

    def send_land(self):
        print('Land...')
        self.pub_land.publish(Empty())

    def send_reset(self):
        print('Reset...')
        self.pub_reset.publish(Empty())
