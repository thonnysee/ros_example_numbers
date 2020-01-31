#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_receive_radio_data(msg):
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('radio_receiver')

    sub = rospy.Subscriber('/FM_98_1', String, callback_receive_radio_data)

    rospy.spin()
