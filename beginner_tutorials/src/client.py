#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.Sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def ask_num(x,y,z):
    rospy.wait_for_service('num_server')
    try:
        num = rospy.ServiceProxy('num_server',Num)
        resp1 = num(x,y,z)
       	return resp1.Sum,resp1.Prod
    except rospy.ServiceException as e:
       	print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
    print("asking the num server for x + y + x",ask_num(x,y,z))
