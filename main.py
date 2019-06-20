from data_loading import load_level, setup_directions, load_signs
from display import show_screen_and_wait, show_2d_table
from player_input import getch
import templates


def main():
    show_intro()
    player = create_character()
    start_game(player)


def show_intro():
    show_screen_and_wait(templates.WELCOME)


def create_character():
    show_screen_and_wait(templates.CHARACTER_CREATION)
    player = {
        "name": "Eisenheim",
        "type": "player",
        "position": {
            'x': 1,
            'y': 3
        },
        "previous_position": {}
    }

    return player


def show_level(level):
    show_2d_table(level)


def get_sign_for(entity_type):
    signs = load_signs()

    return signs[entity_type]


def place_player(character, level):
    x, y = character["position"].values()
    entity_type = character["type"]

    level[y][x] = get_sign_for(entity_type)

    if character["previous_position"]:
        old_x, old_y = character["previous_position"].values()
        level[old_y][old_x] = get_sign_for("empty")


def leave_game():
    show_screen_and_wait(templates.GOODBYE)
    quit(0)


def move(character, direction):
    for coord_key in direction:
        character["previous_position"][coord_key] = character["position"][coord_key]
        character["position"][coord_key] += direction[coord_key]


def start_game(character):
    show_screen_and_wait(templates.GAME_START, character)

    level = load_level()
    directions = setup_directions()

    while True:
        place_player(character, level)
        show_level(level)

        key = getch()

        if key in directions:
            direction = directions[key]
            move(character, direction)
        elif key == "q":
            leave_game()


if __name__ == "__main__":
    main()
