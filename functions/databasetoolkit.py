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
    
    while True:
        entry = buttons.draw_menu(stdscr,
                                  unlocked_db.entries,
                                  is_helper=True,
                                  helper_text="[C]reate Entry | [D]elete Entry | [Q]uit and Save")
        match entry:
            case "c":
                data = []
                questions = ["Title: ",
                             "Username: ",
                             "Password: "]
                
                #got error in group type
                group_names = [group.name for group in unlocked_db.groups]
                selected_group = buttons.draw_menu(stdscr, group_names)

                for question in questions:
                    stdscr.clear()
                    curses.echo()
                    stdscr.addstr(0, 0, question)
                    stdscr.refresh()
                    data.append(stdscr.getstr().decode())

                unlocked_db.add_entry(pykeepass.Group(name=selected_group), data[0], data[1], data[2])
                continue

            case "q":
                unlocked_db.save()
                return db_global_menu(stdscr)
            
            case "d":
                unlocked_db.delete_entry(entry)
                continue
            
            case _:
                stdscr.clear()
                curses.echo()
                stdscr.addstr(0, 0, entry)
                stdscr.refresh()

def db_global_menu(stdscr):
    stdscr.clear()
    contents = list_db(stdscr)
    action = buttons.draw_menu(stdscr,
                               contents,
                               is_helper=True,
                               helper_text="[C]reate | [Q]uit")
    match action:
        case "c":
            db = db_create_menu(stdscr)
            return db_global_menu(stdscr)
        case "q":
            return mainpage.mainpage(stdscr) 
        case _:
            db_menu(stdscr, db=action)
            stdscr.refresh()
