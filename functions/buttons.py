import curses
import passgen3

def inputkey(stdscr):
    key = stdscr.getch()
    return key

def enter_keys():
    KEYS = (curses.KEY_ENTER, 10, 13)
    return KEYS

def menu_items(*items):
    return list(items)

# Run selected menu item
def run_main_menu_item(stdscr, item):

    if item == "Generate Passwords":

        # Open another screen
        stdscr.clear()
        stdscr.addstr(2, 0, passgen3.password_screen(stdscr))
        stdscr.addstr(4, 0, "Password generation finished.")
        stdscr.addstr(5, 0, "Press Enter to return...")

        stdscr.refresh()
        
        while True:
            key = inputkey(stdscr)
            if key in enter_keys():
                stdscr.clear()
                break

    elif item == "Select Database":

        stdscr.clear()
        stdscr.addstr(0, 0, "Database screen not implemented.")
        stdscr.getch()

    elif item == "Settings":

        stdscr.clear()
        stdscr.addstr(0, 0, "Settings screen not implemented.")
        stdscr.getch()

    elif item == "Quit":
        return False

    return True


def draw_menu(stdscr, menu_items):
    curses.curs_set(0)      # Hide cursor
    stdscr.keypad(True)
    stdscr.clear()
    selected = 0

    while True:

        for row, text in enumerate(menu_items):
            if row == selected:
                stdscr.addstr(row, 2, text, curses.A_REVERSE)
            else:
                stdscr.addstr(row, 2, text)

        key = inputkey(stdscr)

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(menu_items)

        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(menu_items)

        elif key in enter_keys():

            selected_item = run_main_menu_item(stdscr, menu_items[selected])

            if not selected_item:
                break

        stdscr.refresh()


