import pykeepass, pathlib, curses, os
import buttons, mainpage

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

#------
# Menu
#------
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


def db_menu(stdscr, db):
    unlocked_db = load_db(stdscr, db)
    entry = buttons.draw_menu(stdscr, unlocked_db.entries)
    return False


def db_global_menu(stdscr):
    contents = list_db(stdscr)

    if contents == []:
        stdscr.clear()
        stdscr.addstr(0, 0, "There are no Database files in your folder,")
        stdscr.addstr(1, 0, "Do you want to create one?")
        stdscr.refresh()
        key = buttons.help_bar(stdscr, text="[Y]es | [N]o")
        if key == ord("y"):
            db = db_create_menu(stdscr)
            db_global_menu(stdscr)
        elif key == ord("n"):
            return mainpage.mainpage(stdscr) 
    else:
        db_path = buttons.draw_menu(stdscr, contents)
        db_menu(stdscr, db=db_path)

