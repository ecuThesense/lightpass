import curses, passgen3

items = [
    "Select Database",
    "Generate Passwords",
    "Settings",
    "Quit"
]

def main_menu(stdscr):

    index = 0

    stdscr.keypad(True)

    while True:

        stdscr.clear()

        for i, item in enumerate(items):

            if i == index:
                stdscr.addstr(i, 2, item, curses.A_REVERSE)

            else:
                stdscr.addstr(i, 2, item)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            index = (index - 1) % len(items)

        elif key == curses.KEY_DOWN:
            index = (index + 1) % len(items)

        elif key in (curses.KEY_ENTER, 10, 13):
            if items[index] == "Generate Passwords":
                print(passgen3.password_screen(stdscr))

                stdscr.addstr(3, 2, "Press Enter to go back")
                
                stdscr.refresh()
                
                key = stdscr.getch()
                
                if key in (curses.KEY_ENTER, 10, 13):
                    continue

            elif items[index] == "Quit":
                break

        stdscr.refresh()

curses.wrapper(main_menu)
