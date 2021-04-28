#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def node2():
    # Create publisher to publish string on the topic /autonomy
    pub = rospy.Publisher('autonomy', String, queue_size=1)

    rospy.init_node('node2', anonymous=True)  # Initialize node2
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish('Fueled By Autonomy')  # Publish the string: 'Fueled By Autonomy'
        rate.sleep()


if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass
