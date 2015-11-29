#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from ir_control.msg import *
import os

def callback(data):
	rospy.loginfo(rospy.get_name() + "\nCOMMAND: %s    |    VALUE: %s    |    ID: %s", data.command, data.value, data.id)
	if data.id == "TV1":
		if data.command == "IR_power": 
		   	os.system('irsend SEND_ONCE LG KEY_POWER')
		elif data.command == "IR_channel":
			if data.value == "1":
				os.system('irsend SEND_ONCE LG KEY_1')
			elif data.value == "2":
				os.system('irsend SEND_ONCE LG KEY_2')
			elif data.value == "3":
				os.system('irsend SEND_ONCE LG KEY_3')
			elif data.value == "4":
				os.system('irsend SEND_ONCE LG KEY_4')
			elif data.value == "5":
				os.system('irsend SEND_ONCE LG KEY_5')
			elif data.value == "6":
				os.system('irsend SEND_ONCE LG KEY_6')
			elif data.value == "7":
				os.system('irsend SEND_ONCE LG KEY_7')
			elif data.value == "8":
				os.system('irsend SEND_ONCE LG KEY_8')
			elif data.value == "9":
				os.system('irsend SEND_ONCE LG KEY_9')
			elif data.value == "10":
				os.system('irsend SEND_ONCE LG KEY_1')
				rate = rospy.Rate(1)
				rate.sleep()
				os.system('irsend SEND_ONCE LG KEY_0')
			elif data.value == "11":
				os.system('irsend SEND_ONCE LG KEY_1')
				rate = rospy.Rate(1)
				rate.sleep()
				os.system('irsend SEND_ONCE LG KEY_1')
		elif data.command == "IR_volume":
			if data.value == "up":
				os.system('irsend SEND_START LG KEY_VOLUMEUP')
				rate = rospy.Rate(2)
				rate.sleep()
				os.system('irsend SEND_STOP LG KEY_VOLUMEUP')
			elif data.value == "down":
				os.system('irsend SEND_START LG KEY_VOLUMEDOWN')
				rate = rospy.Rate(2)
				rate.sleep()
				os.system('irsend SEND_STOP LG KEY_VOLUMEDOWN')
			elif data.value == "little_up":
				os.system('irsend SEND_ONCE LG KEY_VOLUMEUP')
			elif data.value == "little_down":
				os.system('irsend SEND_ONCE LG KEY_VOLUMEDOWN')


#    rospy.loginfo(rospy.get_name() + "ID: %s", data.id")

def listener():
	rospy.Subscriber('remote_control', IRControlMsg, callback)
	rospy.spin()

if __name__ == '__main__':
	rospy.init_node('ir_listener', anonymous = True)
	listener()
