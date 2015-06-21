#!/usr/bin/env python

"""This is the main module of the project where the algorithm is executed."""

_author__ = "L. Miguel Vargas F."
__copyright__ = "Copyright 2015, National Polytechnic School, Ecuador"
__credits__ = ["Mani Monajjemi", "Sika Abarca", "Gustavo Scaglia", "Andres Rosales"]
__license__ = "Noncommercial"
__version__ = "1.0.0"
__maintainer__ = "L. Miguel Vargas F."
__email__ = "lmiguelvargasf@gmail.com"
__status__ = "Development"

from references import *
from position import save_position_into_txt
from constants import *
from controller import *

controller = ARDroneController()

if __name__ == '__main__':
    rospy.init_node('controller_node', anonymous=True)

    rospy.sleep(1)
    print("ready!")
    controller.send_flat_trim()

    controller.send_take_off()
    rospy.sleep(5.0)

    r = rospy.Rate(10)  # 10hz <=> 100 ms
    i = 0
    speed = 0.1
    while not rospy.is_shutdown():
        controller.move_forward(0.05)

        i += 1

        print('For i =', i)
        controller.print_data_test()

        if i == 50:
            speed *= -1
        elif i >= 100:
            break

        r.sleep()

    controller.send_land()

    save_position_into_txt(x_ref_n, "x_n")
    save_position_into_txt(y_ref_n, "y_n")
    save_position_into_txt(z_ref_n, "z_n")

    print("done!")
