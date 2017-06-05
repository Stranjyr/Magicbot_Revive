#!/usr/bin/env python
import curses
from MagicBotMotorFrame import MagicBotMotorFrame
import sys, select, termios, tty

'''getKey method taken from teleop_twist_keyboard
'''

moveBindings = {
				'a':(50, 0 ),
				'd':(0 , 50),
				'w':(50, 50),
				's':(-50, -50)
				}

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key



def main(myscreen):
	#curses setup
	myscreen.border(0)
	myscreen.addstr(5, 17, "WASD and Arrow Keys to Drive")
	myscreen.addstr(7, 30, "Type q to quit")
	myscreen.refresh()
	boost = 1
	defaultSpeed = 20
	lspeed = 0
	rspeed = 0
	mb = MagicBotMotorFrame([(27, 22, 17), (23, 24, 18)])
	mb.start()

	while True:
		key = getKey()
		if key in moveBindings.keys():
			lspeed = moveBindings[key][0]
			rspeed = moveBindings[key][1]
		else:
			lspeed = 0
			rspeed = 0
			if key == 'q':
				break

		mb.move(lspeed, rspeed)
		myscreen.addstr(10, 5, '                                     ')
		myscreen.addstr(10, 20, 'Motors are at {} {}'.format(lspeed, rspeed))
		myscreen.refresh()
	mb.close()

if __name__ == '__main__':
	settings = termios.tcgetattr(sys.stdin)
	curses.wrapper(main)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
