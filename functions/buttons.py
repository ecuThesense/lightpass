import curses, platform, subprocess

def enter_keys():
    KEYS = (curses.KEY_ENTER, 10, 13)
    return KEYS

def clipboard_x(result):
    system = platform.system()
    if system == "Windows": subprocess.run(["clip"], input=result, text=True)
    elif system == "Darwin": subprocess.run(["pbcopy"], input=result, text=True)
    else: subprocess.run(["wl-copy"], input=result, text=True)

def menu_items(*items):
    return list(items)

def draw_menu(stdscr, menu_items):
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.clear()
    selected = 0

    while True:

        for row, text in enumerate(menu_items):
            if row == selected:
                stdscr.addstr(row, 2, text, curses.A_REVERSE)
            else:
                stdscr.addstr(row, 2, text)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(menu_items)

        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(menu_items)

        elif key in enter_keys():
            if not menu_items[selected]: break

            return menu_items[selected]

            stdscr.refresh()


def help_bar(stdscr, text="test"):
    helper, _ = stdscr.getmaxyx()

    while True:
        stdscr.clear()
        stdscr.addstr(helper - 1, 0, text, curses.A_REVERSE)
        stdscr.refresh()
        key = stdscr.getch()
        return key

