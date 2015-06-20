#!/usr/bin/env python
import rospy
from util import take_off
from util import land
from util import flat_trim
from util import forward
from util import backward
from util import reset

if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    print("ready!")
    rospy.sleep(1)

    # reset()
    flat_trim()
    take_off()
    rospy.sleep(5.0)

    print("flying forward..")
    forward(0.05)
    rospy.sleep(5.0)

    print("flying backward..")
    backward(0.05)
    rospy.sleep(5.0)

    land()

    print("done!")
