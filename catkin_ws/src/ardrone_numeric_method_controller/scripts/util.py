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

# Publishers
pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=10)

def take_off():
    pub_takeoff.publish(Empty())

def land():
    pub_land.publish(Empty())

def flat_trim():
    trim = rospy.ServiceProxy('/ardrone/flattrim', std_srvs.srv.Empty)
    trim()
