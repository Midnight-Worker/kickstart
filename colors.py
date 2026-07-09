import curses


def main(stdscr):
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()

    stdscr.addstr(2, 4, "✓ OK", curses.color_pair(1))
    stdscr.addstr(3, 4, "→ Info", curses.color_pair(2))
    stdscr.addstr(4, 4, "! Warnung", curses.color_pair(3))
    stdscr.addstr(5, 4, "✗ Fehler", curses.color_pair(4))

    stdscr.addstr(7, 4, "Taste drücken...")
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
