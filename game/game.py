import character.character_properties
from cell import cell_types
from character import character_actions, action_names, interactions
from data import templates, data_loading
from item import item_types, item_actions, item_properties
from level import level_actions
from position import position_actions
from obstacle import obstacle_types, obstacle_actions, obstacle_properties
from player_interaction import display


def run(get_action_name, input_method):
    show_intro(input_method)
    player = create_player_character(input_method, get_action_name)
    start_game(input_method, player)


def show_intro(input_method):
    display.show_screen_and_wait(input_method, templates.WELCOME)


def create_player_character(input_method, get_action_name):
    display.show_screen_and_wait(input_method, templates.CHARACTER_CREATION)

    name = 'Eisenheim'
    position = position_actions.make_position(1, 3)
    ring = item_actions.create_ring()

    player = character_actions.create_player()
    character.character_properties.set_name(player, name)
    character.character_properties.set_get_action_name(player, get_action_name)
    character_actions.add_walkable(player, cell_types.STONE_FLOOR)
    character_actions.add_interactable(player, item_types.KEY, interactions.pick_up_item)
    character_actions.add_interactable(player, obstacle_types.DOOR, interactions.try_opening_door)
    character.character_properties.set_position(player, position)
    character_actions.add_to_inventory(player, ring)

    return player


def start_game(input_method, player):
    display.show_screen_and_wait(input_method, templates.GAME_START, player)

    level_data, level_view = setup_level()
    directions = data_loading.setup_directions()

    while True:
        perform_frame(input_method, directions, level_data, level_view, player)


def perform_frame(input_method, directions, level_data, level_view, player):
    render_updated_game_view(level_data, level_view, player)
    get_action_name = character.character_properties.get_get_action_name_function(player)
    action_name = get_action_name()
    if action_name in directions:
        perform_character_frame(directions, action_name, level_data, player)
    elif action_name == action_names.QUIT:
        leave_game(input_method)


def setup_level():
    level_raw_view = data_loading.load_level()
    level_data, level_view = data_loading.parse_level_data(level_raw_view)
    add_key_to_level(level_data)
    add_door_to_level(level_data)
    return level_data, level_view


def render_updated_game_view(level_data, level_view, player):
    level_actions.place_character(player, level_data)
    level_actions.refresh_view(level_data, level_view)
    show_level(level_view)
    show_inventory(character.character_properties.get_inventory(player))


def perform_character_frame(directions, key, level_data, player):
    direction = directions[key]
    position = character.character_properties.get_position(player)
    target_position = position_actions.calculate_target_position(position, direction)
    target_cell = level_actions.get_cell_at(level_data, target_position)
    if character_actions.can_interact(player, target_cell):
        character_actions.interact(player, target_cell, level_data)
    if character_actions.can_move(player, target_cell):
        character_actions.move(player, target_position)


def leave_game(input_method):
    display.show_screen_and_wait(input_method, templates.GOODBYE)
    quit(0)


def add_key_to_level(level_data):
    position = position_actions.make_position(1, 2)
    key_data = item_actions.create_key()
    item_properties.set_position(key_data, position)

    level_actions.update_item(level_data, position, key_data)


def add_door_to_level(level_data):
    position = position_actions.make_position(10, 7)
    door = obstacle_actions.create_door()
    obstacle_properties.set_position(door, position)

    level_actions.update_obstacle(level_data, position, door)


def show_level(level):
    display.show_2d_table(level)


def show_inventory(inventory):
    print(templates.INVENTORY)
    for item in inventory:
        print(item)
