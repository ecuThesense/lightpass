import curses
import passgen3, buttons, databasetoolkit

def mainpage(stdscr):
    item = buttons.draw_menu(stdscr, buttons.menu_items(
        "Select Database",
        "Generate Passwords",
        "Settings",
        "Quit"
        )
    )

    match item:
        case "Select Database":
            stdscr.clear()
            databasetoolkit.db_global_menu(stdscr)
        case "Generate Passwords":
            stdscr.clear()
            passgen3.gen_passwords(stdscr)
        case "Settings":
            stdscr.clear()
            stdscr.addstr(0, 0, "Settings screen not implemented.")
            stdscr.getch()
            stdscr.clear()
        case "Quit":
            return False

if __name__ == "__main__":
    curses.wrapper(mainpage)
