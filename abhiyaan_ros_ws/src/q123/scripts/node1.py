#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def node1():
    # Create publisher to publish string on the topic /team_abhiyaan
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=1)

    rospy.init_node('node1', anonymous=True)  # Initialize node1
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish('Team Abhiyaan: ')  # Publish the string: 'Team Abhiyaan'
        rate.sleep()


if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
