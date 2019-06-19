from display import show_screen_and_wait, show_2d_table


def main():
    show_intro()
    player = create_character()
    start_game(player)


def show_intro():
    show_screen_and_wait("Welcome to Rogalik!")


def create_character():
    show_screen_and_wait("=== Character creation ===")
    player = {
        "name": "Eisenheim",
        "type": "player",
        "position": {
            'x': 1,
            'y': 3
        }
    }

    return player


def show_level(level):
    show_2d_table(level)


def load_level():
    return [
        ['#','#','#','#','#','#','#','#','#','#','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','#','#','#','#','#','#','#','#','#','#']
    ]


def get_sign_for(entity_type):
    signs = {
        "player": "@"
    }

    return signs[entity_type]


def place_player(character, level):
    x, y = character["position"].values()
    entity_type = character["type"]

    level[y][x] = get_sign_for(entity_type)


def leave_game():
    show_screen_and_wait("Goodbye, hero!")
    quit(0)


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def start_game(character):
    show_screen_and_wait("Let's play, {name}!".format(**character))

    level = load_level()

    while True:
        place_player(character, level)
        show_level(level)

        key = getch()

        if key == "q":
            leave_game()


if __name__ == "__main__":
    main()
