import character_fields as fields
import data_loading
import display
import player_input
import templates
import character_actions


def main():
    show_intro()
    player = create_character()
    start_game(player)


def show_intro():
    display.show_screen_and_wait(templates.WELCOME)


def create_character():
    display.show_screen_and_wait(templates.CHARACTER_CREATION)
    player = {
        fields.NAME: "Eisenheim",
        fields.TYPE: "player",
        fields.WALKABLES: [
            "empty"
        ],
        fields.POSITION: {
            'x': 1,
            'y': 3
        },
        fields.PREVIOUS_POSITION: {}
    }

    return player


def show_level(level):
    display.show_2d_table(level)


def get_sign_for(entity_type):
    signs = data_loading.load_signs()

    return signs[entity_type]


def place_player(character, level):
    x, y = character[fields.POSITION].values()
    entity_type = character[fields.TYPE]

    level[y][x] = get_sign_for(entity_type)

    if character[fields.PREVIOUS_POSITION]:
        old_x, old_y = character[fields.PREVIOUS_POSITION].values()
        level[old_y][old_x] = get_sign_for("empty")


def leave_game():
    display.show_screen_and_wait(templates.GOODBYE)
    quit(0)


def start_game(character):
    display.show_screen_and_wait(templates.GAME_START, character)

    level = data_loading.load_level()
    level_data = data_loading.parse_level_data(level)
    directions = data_loading.setup_directions()

    while True:
        place_player(character, level)
        show_level(level)

        key = player_input.getch()

        if key in directions:
            direction = directions[key]
            target_position = character_actions.calculate_target_position(character[fields.POSITION], direction)
            x, y = target_position.values()
            target_cell = level_data[y][x]
            if character_actions.can_move(character, target_cell):
                character_actions.move(character, target_position)
        elif key == "q":
            leave_game()


if __name__ == "__main__":
    main()
