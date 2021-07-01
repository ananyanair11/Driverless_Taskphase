#!/usr/bin/env python
import rospy
from ros_task2_msgs.msg import NameAge
from ros_task2_msgs.msg import NameEligibility

def callback(msg):
    Age = msg.Age
    rate = rospy.Rate(2)
    msg1 = NameEligibility()
    msg1.Name = msg.Name
    if Age >= 18:
        msg1.eligibilityStatus = 'eligible voter'
    else:
        msg1.eligibilityStatus = 'ineligible'
    pub.publish(msg1)
    rate.sleep()
    

if __name__ == '__main__':
    rospy.init_node('publish_eligibility')
    pub = rospy.Publisher('/eligibility', NameEligibility, queue_size=10)
    sub = rospy.Subscriber('/nameage', NameAge, callback)
    rospy.spin()
