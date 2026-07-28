import pykeepass, pathlib, curses, os
import functions.buttons

project_root = pathlib.Path(__file__).resolve().parent.parent
dir_path = project_root / "databases"

def list_db(stdscr):

    if not dir_path.exists():
        try: os.mkdir(project_root / "databases")
        except FileExistsError: pass
    
    contents = [str(item) for item in dir_path.glob("*.kdbx") if item.is_file()]
    return contents


def load_db(stdscr, path_db):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Enter a Password of the Database: ")
    stdscr.refresh()
    password = stdscr.getstr().decode()
    stdscr.clear() 
    return pykeepass.PyKeePass(path_db,
                               password)
