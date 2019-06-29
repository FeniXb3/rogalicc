import sys, tty, termios
from data import data_loading


def getch():
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except termios.error:
        return input()


def get_action_by_key():
    key_bindings = data_loading.setup_key_bindings()
    key = getch()
    if key not in key_bindings:
        return None

    return key_bindings[key]
