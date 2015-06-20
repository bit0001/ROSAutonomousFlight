#!/usr/bin/python
import rospy
from std_msgs.msg import Empty

if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    # publish commands (send to quadrotor)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
    pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=10)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty, queue_size=10)

    print("ready!")

    rospy.sleep(1)
    pub_reset.publish()

    print("takeoff..")
    pub_takeoff.publish(Empty())
    rospy.sleep(10.0)

    print("land..")
    pub_land.publish(Empty())

    print("done!")
