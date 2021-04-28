#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def node2():
    pub = rospy.Publisher('autonomy', String, queue_size=10)
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        text = 'Fueled By Autonomy'
        rospy.loginfo(text)
        pub.publish(text)
        rate.sleep()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass
