#!/usr/bin/python
from geometry_msgs.msg import Twist, Vector3
import rospy
from std_msgs.msg import Empty
import std_srvs.srv


def flat_trim():
    trim = rospy.ServiceProxy('/ardrone/flattrim', std_srvs.srv.Empty)
    trim()


if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    # publish commands (send to quadrotor)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
    pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=10)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty, queue_size=10)
    pub_velocity = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    print("ready!")

    rospy.sleep(1)

    if False:
        pub_reset.publish()
        print('RESET')

    flat_trim()
    print('Flat Trim done!')

    print("takeoff..")
    pub_takeoff.publish(Empty())
    rospy.sleep(5.0)

    print("flying right..")
    pub_velocity.publish(Twist(Vector3(0, -0.05, 0), Vector3(0, 0, 0)))
    rospy.sleep(5.0)

    print("flying left..")
    pub_velocity.publish(Twist(Vector3(0, 0.1, 0), Vector3(0, 0, 0)))
    rospy.sleep(10.0)

    print("land..")
    pub_land.publish(Empty())

    print("done!")
