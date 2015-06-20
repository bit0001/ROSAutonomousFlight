#!/usr/bin/env python

"""This is a module that contains useful functions for this project."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi Rob Knight", "Sika Abarca"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

import rospy
from std_msgs.msg import Empty
import std_srvs.srv
from geometry_msgs.msg import Twist, Vector3

# Publishers
pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty, queue_size=10)
pub_land = rospy.Publisher("/ardrone/land", Empty, queue_size=10)
pub_reset = rospy.Publisher("/ardrone/reset", Empty, queue_size=10)
pub_velocity = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def take_off():
    print("Take off...")
    pub_takeoff.publish(Empty())

def land():
    print('Land...')
    pub_land.publish(Empty())

def flat_trim():
    print('Flat trim...')
    trim = rospy.ServiceProxy("/ardrone/flattrim", std_srvs.srv.Empty)
    trim()

def reset():
    print('Reset...')
    pub_reset.publish()

def forward(speed):
    pub_velocity.publish(Twist(Vector3(speed, 0, 0), Vector3(0, 0, 0)))

def backward(speed):
    pub_velocity.publish(Twist(Vector3(-speed, 0, 0), Vector3(0, 0, 0)))