#!/usr/bin/env python3

from __future__ import print_function

from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse, Num, NumResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.A, req.B, (req.A + req.B)))
    return AddTwoIntsResponse(req.A + req.B)

def handle_num(req):
    return NumResponse(req.A * req.B * req.C, req.A + req.B + req.C )


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    s2 = rospy.Service('num_server', Num, handle_num)
    print("Ready for Num service")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
