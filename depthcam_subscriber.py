#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def callback(ros_image):
    global bridge
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print e

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('opencv_depthcam', anonymous=True)
    image_sub = rospy.Subscriber("/camera/color/image_raw",Image,callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    cv2.destroyAllWindows()
