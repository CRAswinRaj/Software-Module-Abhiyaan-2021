#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import String


def callback(t1, t2):
    print(t1.data, t2.data)  # Print data in t1 and t2 adjecently


def listener_node():
    rospy.init_node('listener_node', anonymous=True)
    # Create two subscribers to subscribe to topics on /team_abhiyaan and /autonomy respectively
    text1 = message_filters.Subscriber('team_abhiyaan', String)
    text2 = message_filters.Subscriber('autonomy', String)

    # Sunchronize both subscribers and run the callback function
    ts = message_filters.ApproximateTimeSynchronizer([text1, text2], queue_size=1, slop=0.1, allow_headerless=True)
    ts.registerCallback(callback)

    rospy.spin()


if __name__ == '__main__':
    listener_node()
