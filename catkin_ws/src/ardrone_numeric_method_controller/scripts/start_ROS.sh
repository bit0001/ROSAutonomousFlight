#!/usr/bin/env bash
echo "Starting ROS";
cd;
source /home/m/PycharmProjects/ROSAutonomousFlight/catkin_ws/devel/setup.bash;
roslaunch ardrone_numeric_method_controller ardrone.launch;
