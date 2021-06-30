#!/usr/bin/env python
import rospy
from ros_task1_msgs.msg import NumberInput

if __name__ == '__main__':
    rospy.init_node('ros_publisher')

    pub = rospy.Publisher('/addition', NumberInput, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = NumberInput()
        print "Enter the value for a "
        msg.a = input()
        print "Enter the value for b"
        msg.b = input()
        pub.publish(msg)
        rate.sleep()

    rospy.longinfo("Node was killed")
