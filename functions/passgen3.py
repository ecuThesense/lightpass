import string, secrets, curses

def passgen3(passw_type = 1, passw_lenght = 15):
    letters = string.ascii_letters + string.digits + '!@#$%^&*()'

    with open('words.txt') as f:
        if passw_type == 1: 
            passw = ''.join(secrets.choice(letters) for _ in range(passw_lenght))
    
        elif passw_type == 2:
            words = [word.strip() for word in f]
            passw = '-'.join(secrets.choice(words) for _ in range(passw_lenght))
            
        else:
            print("Wrong Type.")

        return(passw)

def passw_lenght_check(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(2, 2, "How big should your password be: ")
        stdscr.refresh()

        # value = stdscr.getstr(2, 35, 5).decode()
        value = stdscr.getstr().decode()

        try:
            length = int(value)

            if length <= 0:
                stdscr.addstr(4, 2, "Enter a number greater than 0")
                stdscr.getch()
                continue

            return length

        except ValueError:
            stdscr.addstr(4, 2, "Invalid number")
            stdscr.getch()

def password_screen(stdscr):
    index = 0
    stdscr.keypad(True)
    items = [
            "Generate Password",
            "Generate Passphrase",
            "Quit"
            ]

    while True:
        stdscr.clear()

        for i, item in enumerate(items):

            if i == index:
                stdscr.addstr(i, 2, item, curses.A_REVERSE)

            else:
                stdscr.addstr(i, 2, item)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            index = (index - 1) % len(items)

        elif key == curses.KEY_DOWN:
            index = (index + 1) % len(items)

        elif key in (curses.KEY_ENTER, 10, 13):
            if items[index] == "Generate Password":
                stdscr.clear()
                return passgen3(passw_type = 1, passw_lenght = passw_lenght_check(stdscr))
                break

            if items[index] == "Generate Passphrase":
                stdscr.clear()
                return passgen3(passw_type = 2, passw_lenght = passw_lenght_check(stdscr))
                break

        stdscr.refresh()
