#! /usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('radio_transmitter', anonymous = 'true')

    pub = rospy.Publisher('/FM_98_1', String, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = 'Metal Music'
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo('Node has stopped')
