#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class TurtleBot:
    def __init__(self):
        rospy.init_node('turtle_node', anonymous=True)
        self.t1_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.t1_update)  # Subscriber for pose of turtle1
        self.t2_pose_sub = rospy.Subscriber('/turtle2/pose', Pose, self.t2_update)  # Subscriber for pose of turtle2
        self.t2_vel_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)  # Publisher for velocity of turtle2

        self.t1_pose = Pose()  # Initialize pose of turtle1
        self.t2_pose = Pose()  # Initialize pose of turtle2
        self.rate = rospy.Rate(10)
        self.rate.sleep()

    # Update t1_pose
    def t1_update(self, data):
        self.t1_pose = data

    # Update t2_pose
    def t2_update(self, data):
        self.t2_pose = data

    # Find distance turtle 1 and turtle2
    def turtles_distance(self):
        return math.sqrt((self.t1_pose.x - self.t2_pose.x) ** 2 +
                         (self.t1_pose.y - self.t2_pose.y) ** 2)

    # Find angle to steered by turtle2 to move towards turtle1
    def steering_angle(self):
        return math.atan2(self.t1_pose.y - self.t2_pose.y, self.t1_pose.x - self.t2_pose.x)

    # Move turtle 2 as per the problem statement
    def move(self):
        vel_msg = Twist()   # Initialize velocity of turtle 2
        while self.turtles_distance() > 2:
            vel_msg.linear.x = 2 * self.turtles_distance()  # Assign linear velocity of turtle 2
            vel_msg.angular.z = 5 * (self.steering_angle() - self.t2_pose.theta)    # Assign angular velocity of turtle2

            self.t2_vel_pub.publish(vel_msg)    # Publish velocity value to turtle 2

            self.rate.sleep()

        # Turn turtle 2 by 90 degrees
        vel_msg.linear.x = 0
        vel_msg.angular.z = math.pi / 2
        self.t2_vel_pub.publish(vel_msg)
        rospy.sleep(1)

        # Make a quarter circular turn
        vel_msg.linear.x = math.pi
        vel_msg.angular.z = -math.pi / 2
        self.t2_vel_pub.publish(vel_msg)
        rospy.sleep(1)

        # Moving to safe distance
        # Safe distance is 4 units from turtle 1
        while self.turtles_distance() <= 4:
            vel_msg.linear.x = 2 * (4.1 - self.turtles_distance())
            vel_msg.angular.z = 0
            self.t2_vel_pub.publish(vel_msg)

            self.rate.sleep()

        # Bring turtle 1 to rest
        vel_msg.linear.x = 0
        self.t2_vel_pub.publish(vel_msg)

        rospy.spin()


if __name__ == '__main__':
    try:
        bot = TurtleBot()
        bot.move()
    except rospy.ROSInterruptException:
        pass
