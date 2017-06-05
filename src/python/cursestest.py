import curses

def test(myscreen):
	myscreen.border(0)
	myscreen.addstr(5, 25, "Python curses in action!", curses.A_STANDOUT)
	myscreen.addstr(6, 25, "Enter to exit!")
	myscreen.refresh()
	myscreen.getch()


curses.wrapper(test)