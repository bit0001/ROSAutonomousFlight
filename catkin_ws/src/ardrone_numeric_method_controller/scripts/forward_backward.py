#!/usr/bin/env python
from geometry_msgs.msg import Twist, Vector3
import rospy
from std_msgs.msg import Empty
from util import take_off
from util import land
from util import flat_trim

if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    # publish commands (send to quadrotor)
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
    take_off()
    rospy.sleep(5.0)

    print("flying forward..")
    pub_velocity.publish(Twist(Vector3(0.05, 0, 0), Vector3(0, 0, 0)))
    rospy.sleep(5.0)

    print("flying backward..")
    pub_velocity.publish(Twist(Vector3(-0.05, 0, 0), Vector3(0, 0, 0)))
    rospy.sleep(5.0)

    print("land..")
    land()

    print("done!")
