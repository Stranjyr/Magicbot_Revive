#!/usr/bin/env python
from MotorControl import ThreadedMotorControl
import time

class MagicBotMotorFrame:
	def __init__(self, drivers):
		self.leftDriver = ThreadedMotorControl(drivers[0])
		self.rightDriver = ThreadedMotorControl(drivers[1])

	def start(self):
		self.leftDriver.start()
		self.rightDriver.start()

	def move(self, leftSpeed, rightSpeed):
		self.leftDriver.speed = leftSpeed
		self.rightDriver.speed = -rightSpeed

	def close(self):
		self.leftDriver.close()
		self.rightDriver.close()

	#Simple Shortcut commands

	def hardLeft(self, leftSpeed):
		self.move(leftSpeed, 0)

	def hardRight(self, rightSpeed):
		self.move(0, rightSpeed)

	def softLeft(self, speed):
		if speed != 0:
			self.move(speed, speed/2.0)
		else:
			self.stop()

	def softRight(self, speed):
		if speed != 0:
			self.move(speed/2.0, speed)
		else:
			self.stop()

	def stop(self):
		self.move(0, 0)

	def straight(self, speed):
		self.move(speed, speed)

if __name__ == '__main__':
	mb = MagicBotMotorFrame([[27, 22, 17], [23, 24, 18]])
	mb.start()
	#Demo circle
	mb.softRight(20)
	print(1)
	time.sleep(1)

	mb.straight(20)
	print(2)
	time.sleep(1)
	mb.straight(-20)
	print(3)
	time.sleep(1)
	mb.hardLeft(20)
	print(4)
	time.sleep(1)
	mb.stop()
	mb.close()


