import curses
from functions import buttons
import pages.gen_pass_page, pages.db_select_page, pages.settings_page
def mainpage(stdscr):
    while True:
        key, item = buttons.draw_menu(stdscr, buttons.menu_items(
            "Select Database",
            "Generate Passwords",
            "Settings",
            "Quit"
            )
        )

        match item:
            case "Select Database":
                stdscr.clear()
                # databasetoolkit.db_global_menu(stdscr)
                pages.db_select_page.db_global_menu(stdscr)
            case "Generate Passwords":
                stdscr.clear()
                pages.gen_pass_page.gen_passwords(stdscr)
            case "Settings":
                stdscr.clear()
                stdscr.addstr(0, 0, "Settings screen not implemented.")
                stdscr.getch()
                stdscr.clear()
            case "Quit":
                break

if __name__ == "__main__":
    curses.wrapper(mainpage)
