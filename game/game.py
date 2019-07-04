from character import character_actions, action_names, character_properties
from data import templates, data_loading
from item import item_actions
from level import level_actions
from position import position_actions
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

    player = character_actions.create_player(get_action_name)
    character_properties.set_name(player, name)
    character_properties.set_position(player, position)
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
    get_action_name = character_properties.get_get_action_name_function(player)
    action_name = get_action_name()
    if action_name in directions:
        character_actions.perform_character_frame(player, directions, action_name, level_data)
    elif action_name == action_names.QUIT:
        leave_game(input_method)


def setup_level():
    level_raw_view = data_loading.load_level()
    level_data, level_view = data_loading.parse_level_data(level_raw_view)
    level_actions.add_door_to_level_at(level_data, 10, 7, True)
    return level_data, level_view


def render_updated_game_view(level_data, level_view, player):
    level_actions.place_character(player, level_data)
    level_actions.refresh_view(level_data, level_view)
    show_level(level_view)
    show_inventory(character_properties.get_inventory(player))


def leave_game(input_method):
    display.show_screen_and_wait(input_method, templates.GOODBYE)
    quit(0)


def show_level(level):
    display.show_2d_table(level)


def show_inventory(inventory):
    print(templates.INVENTORY)
    for item in inventory:
        print(item)
