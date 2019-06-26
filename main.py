from data import data_loading, templates
from player_interaction import player_input, display
from character import character_actions, character_fields as fields, entity_types
from level import level_actions, position_fields as pos, cell_types, cell_fields, item_types


def main():
    show_intro()
    player = create_player_character()
    start_game(player)


def show_intro():
    display.show_screen_and_wait(templates.WELCOME)


def add_to_inventory(character, item):
    character[fields.INVENTORY].append(item)


def collect(character, item, level_data):
    add_to_inventory(character, item)
    position = item["position"]
    level_actions.update_item(level_data, position, None)

def create_player_character():
    display.show_screen_and_wait(templates.CHARACTER_CREATION)
    player = {
        fields.NAME: "Eisenheim",
        fields.TYPE: entity_types.PLAYER,
        fields.INVENTORY: [],
        fields.WALKABLES: [
            cell_types.EMPTY
        ],
        fields.INTERACTABLES: {
            item_types.KEY: collect
        },
        fields.POSITION: {
            pos.X: 1,
            pos.Y: 3
        },
        fields.PREVIOUS_POSITION: {}
    }

    return player


def show_level(level):
    display.show_2d_table(level)


def leave_game():
    display.show_screen_and_wait(templates.GOODBYE)
    quit(0)


def can_interact_with_item(character, item_data):
    if not item_data:
        return False

    item_type = item_data["type"]
    return item_type in character[fields.INTERACTABLES]


def can_interact(character, target_cell):
    if can_interact_with_item(character, target_cell[cell_fields.ITEM]):
        return True

    return False


def interact(character, target_cell, level_data):
    item_data = target_cell[cell_fields.ITEM]

    if not item_data:
        return

    item_type = item_data["type"]
    action = character[fields.INTERACTABLES][item_type]
    action(character, item_data, level_data)


def start_game(player):
    display.show_screen_and_wait(templates.GAME_START, player)

    level_view = data_loading.load_level()
    level_data = data_loading.parse_level_data(level_view)
    directions = data_loading.setup_directions()

    while True:
        level_actions.place_character(player, level_data)
        level_actions.refresh_view(level_data, level_view)
        show_level(level_view)

        key = player_input.getch()

        if key in directions:
            direction = directions[key]
            target_position = character_actions.calculate_target_position(player[fields.POSITION], direction)
            target_cell = level_actions.get_cell_at(level_data, target_position)

            if can_interact(player, target_cell):
                interact(player, target_cell, level_data)

            if character_actions.can_move(player, target_cell):
                character_actions.move(player, target_position)
        elif key == "q":
            leave_game()


if __name__ == "__main__":
    main()
