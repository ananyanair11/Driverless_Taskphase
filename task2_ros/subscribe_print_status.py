#!/usr/bin/env python
import rospy
from ros_task2_msgs.msg import NameEligibility

def callback(msg1):
    print msg1.Name
    print msg1.eligibilityStatus

if __name__ == '__main__':
    rospy.init_node('subscribe_print_status')
    sub = rospy.Subscriber('/eligibility', NameEligibility, callback)
    rospy.spin()
