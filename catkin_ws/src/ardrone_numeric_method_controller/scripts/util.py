#!/usr/bin/env python

"""This is a module that contains useful functions for this project."""


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

def left(speed):
    pub_velocity.publish(Twist(Vector3(0, speed, 0), Vector3(0, 0, 0)))

def right(speed):
    pub_velocity.publish(Twist(Vector3(0, -speed, 0), Vector3(0, 0, 0)))

def up(speed):
    pub_velocity.publish(Twist(Vector3(0, 0, speed), Vector3(0, 0, 0)))

def down(speed):
    pub_velocity.publish(Twist(Vector3(0, 0, -speed), Vector3(0, 0, 0)))

def clockwise(speed):
    pub_velocity.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, -speed)))

def counterclockwise(speed):
    pub_velocity.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, speed)))

def get_array_from_file(path_to_file):
    with open(path_to_file) as opened_file:
        content = opened_file.read()
    return content.split('\n')[:-1]

def save_array_into_file(array, path_to_file):
    created_file = open(path_to_file, 'w+')

    for item in array:
        created_file.write("%s\n" % item)
