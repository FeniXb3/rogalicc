def main():
    show_intro()
    player = create_character()
    start_game(player)


def show_intro():
    print("Welcome to Rogalik!")


def create_character():
    print("=== Character creation ===")
    player = {
        "name": "Eisenheim"
    }

    return player


def start_game(character):
    print("Let's play, {name}!".format(**character))


if __name__ == "__main__":
    main()
