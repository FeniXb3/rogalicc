import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    input("Press Enter to continue...")


def show_screen(content):
    clear_screen()
    print(content)


def show_screen_and_wait(content):
    show_screen(content)
    wait()
