import pykeepass, pathlib, curses, os
import functions.buttons

project_root = pathlib.Path(__file__).resolve().parent.parent
dir_path = project_root / "databases"

def create_db(name,
              password, 
              keyfile=None,
              transformed_key=None):
    db_path = project_root / "databases" / f"{name}.kdbx"

    pykeepass.create_database(
        str(db_path),
        password=password,
        keyfile=keyfile,
        transformed_key=transformed_key,
        )

def db_create_menu(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Enter a Name of New Database: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Enter a Password of New Database: ")
    stdscr.refresh()
    password = stdscr.getstr().decode()
    stdscr.clear()
    
    create_db(name, password)
