import pykeepass, pathlib, curses, os
import functions.buttons, functions.databasetoolkit, functions.passgen3
import pages.gen_pass_page

def db_menu(stdscr, db):
    unlocked_db = functions.databasetoolkit.load_db(stdscr, db)
    
    while True:
        key, entry = functions.buttons.draw_menu(stdscr,
                                       unlocked_db.entries,
                                       is_helper=True,
                                       helper_text="[C]reate Entry | [D]elete Entry | [Q]uit and Save",
                                       is_upper=True,
                                       upper_text=f"{db}",
                                       height=2)
        match key:
            case "c":
                data = []
                questions = ["Title: ",
                             "Username: ",
                             "Password: "]
                
                key, selected_group = functions.buttons.draw_menu(stdscr,
                                                   unlocked_db.groups,
                                                   display=lambda g: g.name)

                for question in questions:
                    stdscr.clear()
                    curses.echo()
                    if question == "Password: ":
                        key, selected_option = functions.buttons.draw_menu(stdscr,
                                                                           ["Yes",
                                                                            "No"],
                                                                           is_upper=True,
                                                                           upper_text="Do you want to Generate password?",
                                                                           height=2)
                        match selected_option:
                            case "Yes":
                                data.append(pages.gen_pass_page.gen_passwords(stdscr))
                            case "No":
                                data.apdend(stdscr.getstr().decode())
                        stdscr.refresh()
                    else:
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
                return pages.db_select_page.db_global_menu(stdscr)
            
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

                key, selected = functions.buttons.draw_menu(stdscr,
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
                        functions.buttons.clipboard_x(getattr(entry, attribute))
                        # continue
                
                stdscr.getch()
                stdscr.clear()
                continue
