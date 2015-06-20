#!/usr/bin/env python
import rospy
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3
from util import flat_trim

t = 0


def callback(navdata):
    global t
    t = navdata
    # t = navdata.header.stamp.to_sec()
    # print("received odometry message: time=%f battery=%f vx=%f vy=%f z=%f yaw=%f"%(t,navdata.batteryPercent,navdata.vx,navdata.vy,navdata.altd,navdata.rotZ))


if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)

    # subscribe to navdata (receive from quadrotor)
    rospy.Subscriber("/ardrone/navdata", Navdata, callback)

    # publish commands (send to quadrotor)
    pub_velocity = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
    pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=10)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty, queue_size=10)

    rospy.sleep(1.0)
    print("ready!")
    flat_trim()

    print("takeoff..")
    pub_takeoff.publish(Empty())
    rospy.sleep(5.0)

    r = rospy.Rate(10)  # 10hz <=> 100 ms
    i = 0
    speed = 0.1
    while not rospy.is_shutdown():
        pub_velocity.publish(Twist(Vector3(speed, 0, 0), Vector3(0, 0, 0)))
        print("received odometry message for i = {0:d}: time={1:f} battery={2:f} vx={3:f} vy={4:f} z={5:f} yaw={6:f}"
              .format(i, t.header.stamp.to_sec(), t.batteryPercent, t.vx, t.vy, t.altd, t.rotZ))

        i += 1

        if i == 50:
            speed *= -1
        elif i >= 100:
            break

        r.sleep()

    pub_land.publish(Empty())
