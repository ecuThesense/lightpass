import curses
import functions.buttons, functions.databasetoolkit
import pages.db_page, pages.db_create_page

def db_global_menu(stdscr):
    stdscr.clear()
    contents = functions.databasetoolkit.list_db(stdscr)
    key, action = functions.buttons.draw_menu(stdscr,
                               contents,
                               is_helper=True,
                               helper_text="[C]reate | [Q]uit")
    match key:
        case "c":
            db = pages.db_create_page.db_create_menu(stdscr)
            return pages.db_global_menu(stdscr)
        case "q":
            return 
        case _:
            pages.db_page.db_menu(stdscr, db=action)
            stdscr.refresh()
