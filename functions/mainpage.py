import curses
import passgen3, buttons, interface

MENU_ITEMS = buttons.menu_items(
    "Select Database",
    "Generate Passwords",
    "Settings",
    "Quit"
    )

def main(stdscr):
    buttons.draw_menu(stdscr, MENU_ITEMS)

curses.wrapper(main)

#if __name__ == "__main__":
#    curses.wrapper(main)
