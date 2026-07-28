import curses
import functions.buttons, functions.passgen3

def gen_passwords(stdscr):
    key, item = functions.buttons.draw_menu(stdscr,
                                            functions.buttons.menu_items(
                                                "Generate Password",
                                                "Generate Passphrase",
                                                "Quit"
                                                )
                                            )

    match item:
        case "Generate Password":
            return str(functions.passgen3.fin_passwords(stdscr,
                                                    functions.passgen3.passgen3(passw_type = 1,
                                                                                passw_lenght = functions.passgen3.passw_lenght_check(stdscr))))
        case "Generate Passphrase":
            return str(functions.passgen3.fin_passwords(stdscr,
                                                    functions.passgen3.passgen3(passw_type = 2,
                                                                                passw_lenght = functions.passgen3.passw_lenght_check(stdscr))))
        case "Quit":
            return
