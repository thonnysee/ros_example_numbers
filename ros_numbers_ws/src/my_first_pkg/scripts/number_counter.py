#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_receive_radio_data(msg):
    complete_msg = "Number Counter: " + msg
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('number_counter')

    sub = rospy.Subscriber('/number', String, callback_receive_radio_data)

    rospy.spin()
