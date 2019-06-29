from character import character_actions, character_fields as fields, entity_types, interactions
from data import data_loading, templates
from item import item_fields
from item import item_types
from level import level_actions, position_fields as pos, cell_types
from obstacle import obstacle_fields, obstacle_types
from player_interaction import player_input, display


def main():
    show_intro()
    player = create_player_character()
    start_game(player)


def show_intro():
    display.show_screen_and_wait(templates.WELCOME)


def create_player_character():
    display.show_screen_and_wait(templates.CHARACTER_CREATION)
    player = {
        fields.NAME: "Eisenheim",
        fields.TYPE: entity_types.PLAYER,
        fields.INVENTORY: [
            {
                item_fields.TYPE: item_types.RING,
                item_fields.POSITION: None
            }
        ],
        fields.WALKABLES: [
            cell_types.STONE_FLOOR
        ],
        fields.INTERACTABLES: {
            item_types.KEY: interactions.pick_up_item,
            obstacle_types.DOOR: interactions.try_opening_door
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


def add_key_to_level(level_data):
    position = {
        pos.X: 1,
        pos.Y: 2
    }
    key_data = {
        item_fields.TYPE: item_types.KEY,
        item_fields.POSITION: position
    }

    level_actions.update_item(level_data, position, key_data)


def show_inventory(inventory):
    print(templates.INVENTORY)
    for item in inventory:
        print(item)


def add_door_to_level(level_data):
    position = {
        pos.X: 10,
        pos.Y: 7
    }
    door_data = {
        obstacle_fields.TYPE: "door",
        obstacle_fields.POSITION: position
    }

    level_actions.update_obstacle(level_data, position, door_data)


def start_game(player):
    display.show_screen_and_wait(templates.GAME_START, player)

    level_data, level_view = setup_level()
    directions = data_loading.setup_directions()

    while True:
        render_updated_game_view(level_data, level_view, player)

        key = player_input.getch()

        if key in directions:
            perform_character_frame(directions, key, level_data, player)
        elif key == "q":
            leave_game()


def perform_character_frame(directions, key, level_data, player):
    direction = directions[key]
    target_position = character_actions.calculate_target_position(player[fields.POSITION], direction)
    target_cell = level_actions.get_cell_at(level_data, target_position)
    if character_actions.can_interact(player, target_cell):
        character_actions.interact(player, target_cell, level_data)
    if character_actions.can_move(player, target_cell):
        character_actions.move(player, target_position)


def render_updated_game_view(level_data, level_view, player):
    level_actions.place_character(player, level_data)
    level_actions.refresh_view(level_data, level_view)
    show_level(level_view)
    show_inventory(player[fields.INVENTORY])


def setup_level():
    level_raw_view = data_loading.load_level()
    level_data, level_view = data_loading.parse_level_data(level_raw_view)
    add_key_to_level(level_data)
    add_door_to_level(level_data)
    return level_data, level_view


if __name__ == "__main__":
    main()
