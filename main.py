import curses


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 4, "Hallo pycurses!")
    stdscr.addstr(4, 4, "Taste drücken zum Beenden...")
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
