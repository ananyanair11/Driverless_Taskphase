#!/usr/bin/env python

import rospy
from ros_task2_msgs.msg import NameAge

if __name__ == '__main__':
    rospy.init_node('publish_name_age')

    pub = rospy.Publisher('/nameage', NameAge, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = NameAge()
        print "Enter Name"
        msg.Name = raw_input()
        print "Enter age"
        msg.Age = input()
        pub.publish(msg)
        rate.sleep()
