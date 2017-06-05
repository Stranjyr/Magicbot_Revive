#!/usr/bin/env python
import curses
#from MagicBotMotorFrame import MagicBotMotorFrame as MBMFrame
import pygame, sys, os
from pygame.locals import *


def main(myscreen):
	#curses setup
	myscreen.border(0)
	myscreen.addstr(5, 17, "WASD and Arrow Keys to Drive")
	myscreen.addstr(6, 25, "Hold Shift to boost")
	myscreen.addstr(7, 30, "Type q to quit")
	myscreen.refresh()
	pygame.init()

	os.environ["SDL_VIDEODRIVER"] = "dummy"
	screen = pygame.display.set_mode((1, 1))
	#mb = MBMFrame([(17, 18, 19), (5, 4, 3)])
	boost = 1
	defaultSpeed = 20
	lspeed = 0
	rspeed = 0
	#mb.start()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_q:
					pygame.quit()
					sys.exit()
				elif event.key == K_w or event.key == K_UP:
					lspeed += defaultSpeed
					rspeed += defaultSpeed

				elif event.key == K_s or event.key == K_DOWN:
					lspeed += -defaultSpeed
					rspeed += -defaultSpeed

				elif event.key == K_d or event.key == K_RIGHT:
					rspeed += defaultSpeed	

				elif event.key == K_a or event.key == K_LEFT:
					lspeed += defaultSpeed

				elif event.key == K_RSHIFT or event.key == K_LSHIFT:
					boost = 2
			elif event.type == KEYUP:
				if event.key == K_w or event.key == K_UP:
					lspeed -= defaultSpeed
					rspeed -= defaultSpeed

				elif event.key == K_s or event.key == K_DOWN:
					lspeed -= -defaultSpeed
					rspeed -= -defaultSpeed

				elif event.key == K_d or event.key == K_RIGHT:
					rspeed -= defaultSpeed	

				elif event.key == K_a or event.key == K_LEFT:
					lspeed -= defaultSpeed

				elif event.key == K_RSHIFT or event.key == K_LSHIFT:
					boost = 1
		#mb.move(lspeed*boost, rspeed*boost)
		myscreen.addstr(10, 25, "                                        ")
		myscreen.addstr(10, 25, "Speeds : {} {}".format(lspeed*boost, rspeed*boost))
		myscreen.refresh()

if __name__ == '__main__':
	curses.wrapper(main)
