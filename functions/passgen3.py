import string, secrets, curses, tkinter
import buttons, mainpage

def passgen3(passw_type = 1, passw_lenght = 15):
    letters = string.ascii_letters + string.digits + '!@#$%^&*()'

    with open('words.txt') as f:
        match passw_type:
            case 1:
                passw = ''.join(secrets.choice(letters) for _ in range(passw_lenght))
                return(passw)
            case 2:
                words = [word.strip() for word in f]
                passw = '-'.join(secrets.choice(words) for _ in range(passw_lenght))
                return(passw)

def passw_lenght_check(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "How big should your password be: ")
        stdscr.refresh()

        # value = stdscr.getstr(2, 35, 5).decode()
        value = stdscr.getstr().decode()

        try:
            length = int(value)

            if length <= 0:
                stdscr.addstr(1, 0, "Enter a number greater than 0")
                stdscr.getch()
                continue

            return length

        except ValueError:
            stdscr.addstr(1, 0, "Invalid number")
            stdscr.getch()

def fin_passwords(stdscr, result):
    buttons.clipboard_x(result)

    stdscr.clear()
    stdscr.addstr(2, 0, result)
    stdscr.addstr(4, 0, "Password generation finished and copied into clipboard.")
    stdscr.addstr(5, 0, "Press Any key to return...")
    stdscr.refresh()

    stdscr.getch()
    stdscr.clear()
    return mainpage.mainpage(stdscr)

def gen_passwords(stdscr):
    item = buttons.draw_menu(stdscr, buttons.menu_items(
        "Generate Password",
        "Generate Passphrase",
        "Quit"
        )
    )

    match item:
        case "Generate Password":
            return fin_passwords(stdscr, passgen3(passw_type = 1, passw_lenght = passw_lenght_check(stdscr)))

        case "Generate Passphrase":
            return fin_passwords(stdscr, passgen3(passw_type = 2, passw_lenght = passw_lenght_check(stdscr)))

        case "Quit":
            return mainpage.mainpage(stdscr) 

