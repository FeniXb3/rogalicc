from character import character_actions, character_fields as fields, entity_types, interactions, action_names
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

    name = 'Eisenheim'
    entity_type = entity_types.PLAYER
    get_action_name = player_input.get_action_by_key
    position = {
        pos.X: 1,
        pos.Y: 3
    }
    ring = {
        item_fields.TYPE: item_types.RING,
        item_fields.POSITION: None
    }

    player = data_loading.load_entity_template("character")
    character_actions.set_name(player, name)
    character_actions.set_type(player, entity_type)
    character_actions.set_get_action_name(player, get_action_name)
    character_actions.add_walkable(player, cell_types.STONE_FLOOR)
    character_actions.add_interactable(player, item_types.KEY, interactions.pick_up_item)
    character_actions.add_interactable(player, obstacle_types.DOOR, interactions.try_opening_door)
    character_actions.set_position(player, position)
    character_actions.add_to_inventory(player, ring)

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
        obstacle_fields.TYPE: obstacle_types.DOOR,
        obstacle_fields.POSITION: position
    }

    level_actions.update_obstacle(level_data, position, door_data)


def start_game(player):
    display.show_screen_and_wait(templates.GAME_START, player)

    level_data, level_view = setup_level()
    directions = data_loading.setup_directions()

    while True:
        render_updated_game_view(level_data, level_view, player)

        action_name = player[fields.GET_ACTION_NAME]()
        if action_name in directions:
            perform_character_frame(directions, action_name, level_data, player)
        elif action_name == action_names.QUIT:
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
