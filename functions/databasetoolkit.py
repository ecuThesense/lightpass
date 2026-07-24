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
        key, entry = buttons.draw_menu(stdscr,
                                       unlocked_db.entries,
                                       is_helper=True,
                                       helper_text="[C]reate Entry | [D]elete Entry | [Q]uit and Save")
        match key:
            case "c":
                data = []
                questions = ["Title: ",
                             "Username: ",
                             "Password: "]
                
                selected_group = buttons.draw_menu(stdscr,
                                                   unlocked_db.groups,
                                                   display=lambda g: g.name)

                for question in questions:
                    stdscr.clear()
                    curses.echo()
                    stdscr.addstr(0, 0, question)
                    stdscr.refresh()
                    data.append(stdscr.getstr().decode())

                unlocked_db.add_entry(selected_group,
                                      data[0],
                                      data[1],
                                      data[2])
                continue

            case "q":
                unlocked_db.save()
                return db_global_menu(stdscr)
            
            case "d":
                unlocked_db.delete_entry(entry)
                stdscr.refresh()
                continue
            
            case "enter":
                stdscr.clear()
                curses.echo()
                fields = [
                        ("Title", "title"),
                        ("Username", "username"),
                        ("Password", "password"),
                        ("URL", "url"),
                        ("Notes", "notes"),
                        ("OTP", "otp"),
                        ("Tags:", "tags"),
                        ("Expires", "expires"),
                        ("Creation Time", "expiry_time"),
                        ]

                key, selected = buttons.draw_menu(stdscr,
                                         fields,
                                         display=lambda f: f"{f[0]}: {getattr(entry, f[1])}",
                                         is_helper=True,
                                         helper_text="[E]dit | [D]elete | [Enter] Copy | [Q]uit")
                stdscr.refresh()
                match key:
                    case "e":
                        label, attribute = selected
                        stdscr.clear()
                        curses.echo()
                        stdscr.addstr(0, 0, f"New {label}: ")
                        new_value = stdscr.getstr().decode()
                        setattr(entry, attribute, new_value)
                        stdscr.refresh()
                        continue
                    case "q":
                        continue
                    case "d":
                        unlocked_db.delete_entry(entry)
                        stdscr.refresh()
                        continue
                    case "enter":
                        label, attribute = selected
                        buttons.clipboard_x(getattr(entry, attribute))
                        # continue
                
                stdscr.getch()
                stdscr.clear()
                continue

def db_global_menu(stdscr):
    stdscr.clear()
    contents = list_db(stdscr)
    key, action = buttons.draw_menu(stdscr,
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
