#!/usr/bin/env python

import rospy
from util import take_off
from util import land
from util import flat_trim
from util import forward
from util import backward
from util import reset
from util import left
from util import right
from util import up
from util import down
from util import counterclockwise
from util import clockwise

if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    rospy.sleep(1)
    print("ready!")

    flat_trim()
    take_off()
    rospy.sleep(5.0)
    clockwise(0.5)
    rospy.sleep(6.0)
    land()

    print("done!")
