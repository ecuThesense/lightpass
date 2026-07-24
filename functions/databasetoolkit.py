import pykeepass, pathlib, curses, os
import buttons, mainpage

project_root = pathlib.Path(__file__).resolve().parent.parent
dir_path = project_root / "databases"

def create_db(name,
              password, 
              keyfile=None,
              transformed_key=None):
    with open(project_root / "databases" / name, "x") as file:
        file.write(pykeepass.create_database(f"{name}.kdbx",
                                             password,
                                             keyfile,
                                             transformed_key))
        file.close()


def list_db(stdscr):

    if not dir_path.exists():
        try: os.mkdir(project_root / "databases")
        except FileExistsError: pass
    
    contents = [str(item) for item in dir_path.glob("*.kdbx") if item.is_file()]
    return contents


def load_db(path_db,
            password,
            keyfile=None,
            transformed_key=None):
    return pykeepass.PyKeePass(path_db,
                               password,
                               keyfile,
                               transformed_key)

#------
# Menu
#------
def db_create_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter a Name of New Database: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter a Password of New Database: ")
    stdscr.refresh()
    password = stdscr.getstr().decode()
    stdscr.clear()
    
    create_db(name, password)


def db_menu(stdscr, db):
    unlocked_db = load_db(db)
    entry = buttons.draw_menu(stdscr, unlocked_db.entries)
    return False


def db_global_menu(stdscr):
    contents = list_db(stdscr)

    if contents == []:
        stdscr.clear()
        stdscr.addstr(0, 0, "There are no DB files in folder,")
        stdscr.addstr(1, 0, "Do you want to create one?")
        stdscr.refresh()
        stdscr.getch()
        key = buttons.help_bar(stdscr, text="[Y]es | [N]o")
        if key == ord("y"):
            db = db_create_menu(stdscr)
        elif key == ord("n"):
            return mainpage.mainpage(stdscr) 
    else:
        db_path = buttons.draw_menu(stdscr, contents)
        db_menu(db=db_path)

