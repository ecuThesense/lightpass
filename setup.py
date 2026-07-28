import curses
import pages.mainpage

if __name__ == "__main__":
    curses.wrapper(pages.mainpage.mainpage)
