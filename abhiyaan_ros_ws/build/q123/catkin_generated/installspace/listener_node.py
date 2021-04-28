#!/usr/bin/env python3

import rospy
import message_filters
from std_msgs.msg import String


def callback(t1, t2):
    print(t1.data, t2.data)
    
  

def listener_node():
    rospy.init_node('listener_node', anonymous=True)
    text1 = message_filters.Subscriber('team_abhiyaan', String)
    text2 = message_filters.Subscriber('autonomy', String)
    
    ts = message_filters.ApproximateTimeSynchronizer([text1, text2], queue_size=10, slop=0.1, allow_headerless=True)
    ts.registerCallback(callback)
    rospy.spin()
    

if __name__ == '__main__':
    listener_node()
