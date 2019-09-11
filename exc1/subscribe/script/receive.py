#!/usr/bin/env python
import rospy
from  std_msgs.msg import Int32

def receive():
    rospy.init_node('receive',anonymous=True)
    rospy.Subscriber("mukhedkar", Int32, callback)

    rospy.spin()


def callback(msg):
    rospy.loginfo("listener reading %s", msg.data)
    transmit(msg.data)


def transmit(input):
    pub = rospy.Publisher('kthfs/result', Int32, queue_size=10)
    rate=rospy.Rate(20)
    q=0.15
    n=input/q
    rospy.loginfo("final number %s time %s", n, rospy.get_time())
    pub.publish(n)
    rate.sleep()
    

if __name__ == '__main__':
    receive()

