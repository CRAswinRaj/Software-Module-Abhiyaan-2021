#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def node1():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        text = 'Team Abhiyaan: '
        rospy.loginfo(text)
        pub.publish(text)
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
