#! /usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('number_publisher', anonymous = 'true')

    pub = rospy.Publisher('/number', String, queue_size=10)

    rate = rospy.Rate(2)
    i = 0

    while not rospy.is_shutdown():
        msg = String()
        i += 1
        msg.data = str(i)
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo('Node has stopped')
