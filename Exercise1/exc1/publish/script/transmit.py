#!/usr/bin/env python

import rospy
from  std_msgs.msg import Int32

def transmit():
    pub = rospy.Publisher('mukhedkar', Int32, queue_size=10)
    rospy.init_node('transmit', anonymous=True)
    rate=rospy.Rate(20)

    n=0
    while not rospy.is_shutdown():
        rospy.loginfo("number %s time %s",n,rospy.get_time())
        pub.publish(n)
        n=n+4
        rate.sleep()


if __name__ == '__main__':
    try :
        transmit()
    except rospy.ROSInterruptException:
        pass




