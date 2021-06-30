#!/usr/bin/env python
import rospy
from ros_task1_msgs.msg import NumberInput

def callback(msg):
    a = msg.a
    b = msg.b
    Sum = a+b
    print "The sum is: ", Sum

if __name__ == '__main__':
    rospy.init_node('ros_subscriber')

    sub = rospy.Subscriber('/addition', NumberInput, callback)

    rospy.spin()
