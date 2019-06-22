import character_fields as fields
import data_loading
import display
import player_input
import templates
import character_actions
import level_actions
import position_fields as pos


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
            pos.X: 1,
            pos.Y: 3
        },
        fields.PREVIOUS_POSITION: {}
    }

    return player


def show_level(level):
    display.show_2d_table(level)


def get_sign_for(entity_type):
    signs = data_loading.load_signs()

    return signs[entity_type]


def leave_game():
    display.show_screen_and_wait(templates.GOODBYE)
    quit(0)


def start_game(character):
    display.show_screen_and_wait(templates.GAME_START, character)

    level = data_loading.load_level()
    level_data = data_loading.parse_level_data(level)
    directions = data_loading.setup_directions()

    while True:
        level_actions.place_character(character, level_data)
        level_actions.refresh_view(level_data, level)
        show_level(level)

        key = player_input.getch()

        if key in directions:
            direction = directions[key]
            target_position = character_actions.calculate_target_position(character[fields.POSITION], direction)
            target_cell = level_actions.get_cell_at(level_data, target_position)
            if character_actions.can_move(character, target_cell):
                character_actions.move(character, target_position)
        elif key == "q":
            leave_game()


if __name__ == "__main__":
    main()
