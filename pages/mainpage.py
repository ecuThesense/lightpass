import curses #Builtin
import functions.buttons #Function
import pages.gen_pass_page, pages.db_select_page, pages.settings_page #Pages
def mainpage(stdscr):
    while True:
        key, item = functions.buttons.draw_menu(stdscr,
                                                functions.buttons.menu_items(
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
