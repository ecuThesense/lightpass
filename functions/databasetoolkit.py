import pykeepass, pathlib, curses
import buttons

project_root = pathlib.Path(__file__).resolve().parent.parent
dir_path = project_root / "databases"

def create_db(name,
              password, 
              keyfile=None,
              transformed_key=None):
    
    return pykeepass.create_database(f"{name}.kdbx",
                                     password,
                                     keyfile,
                                     transformed_key)

def list_db(stdscr):

    if not dir_path.exists(): return None # Add creation func
    
    contents = [str(item) for item in dir_path.glob("*.kdbx") if item.is_file()]
    db = buttons.draw_menu(stdscr, contents)
    return db


def load_db(path_db, password):
    return pykeepass.PyKeePass(path_db, password)
