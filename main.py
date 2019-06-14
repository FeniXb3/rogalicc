from display import show_screen_and_wait


def main():
    show_intro()
    player = create_character()
    start_game(player)


def show_intro():
    show_screen_and_wait("Welcome to Rogalik!")


def create_character():
    show_screen_and_wait("=== Character creation ===")
    player = {
        "name": "Eisenheim"
    }

    return player


def start_game(character):
    show_screen_and_wait("Let's play, {name}!".format(**character))


if __name__ == "__main__":
    main()
