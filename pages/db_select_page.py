import curses
import functions.buttons, functions.databasetoolkit

def db_global_menu(stdscr):
    stdscr.clear()
    contents = list_db(stdscr)
    key, action = functions.buttons.draw_menu(stdscr,
                               contents,
                               is_helper=True,
                               helper_text="[C]reate | [Q]uit")
    match key:
        case "c":
            db = functions.databasetoolkit.db_create_menu(stdscr)
            return db_global_menu(stdscr)
        case "q":
            return 
        case _:
            functions.databasetoolkit.db_menu(stdscr, db=action)
            stdscr.refresh()
