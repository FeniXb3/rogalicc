import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    input("Press Enter to continue...")


def show_screen(content):
    clear_screen()
    print(content)


def show_screen_and_wait(template, data=None):
    if data is None:
        data = {}
    show_screen(template.format(**data))
    wait()


def show_2d_table(table):
    clear_screen()
    for row in table:
        for cell in row:
            print(cell, end='')
        print()
