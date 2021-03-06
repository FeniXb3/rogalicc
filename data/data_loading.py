import json
from queue import Queue

from cell import cell_properties
from data import signs
from level import level_actions, level_properties
from obstacle import obstacle_types
from position import position_actions


def load_level():
    basic_view = []
    with open('resources/levels/basic_level.rll') as f:
        for line in f:
            row = list(line.strip())
            basic_view.append(row)

    return basic_view


def load_action_sequence(sequence_name):
    action_sequence = Queue()
    with open(f'resources/test_data/test_action_sequences/{sequence_name}') as f:
        for action_name in f:
            action_sequence.put(action_name.strip())

    return action_sequence


def load_setting(setting_name):
    return load_json_resource('settings', setting_name)


def load_json_resource(resource_type, resource_name):
    resource_path = f'resources/{resource_type}/{resource_name}.json'
    with open(resource_path) as f:
        setting = json.load(f)
    return setting


def setup_directions():
    directions = load_setting('directions')

    return directions


def parse_level_data(level_raw_view):
    level_data = level_actions.create_level()
    level_view = []

    for y, row in enumerate(level_raw_view):
        data_row = []
        level_properties.get_cells(level_data).append(data_row)
        view_row = []
        level_view.append(view_row)
        for x, sign in enumerate(row):
            cell = parse_cell(sign, x, y)
            data_row.append(cell)
            try_parsing_obstacle(level_data, sign, x, y)
            try_parsing_item(level_data, sign, x, y)

            view_row.append(None)
            level_actions.queue_cell_update(level_data, cell)

    return level_data, level_view


def try_parsing_obstacle(level_data, sign, x, y):
    obstacle_type = signs.get_obstacle_parse_type_by_sign(sign)
    if obstacle_type:
        obstacle_adding_function = level_actions.get_adding_function_for(level_data, obstacle_type)
        obstacle_adding_function(level_data, x, y)


def try_parsing_item(level_data, sign, x, y):
    item_type = signs.get_item_type_by_sign(sign)
    if item_type:
        item_adding_function = level_actions.get_adding_function_for(level_data, item_type)
        item_adding_function(level_data, x, y)


def parse_cell(cell_sign, x, y):
    position = position_actions.make_position(x, y)

    cell_type = signs.get_cell_type_by_sign(cell_sign)
    cell = load_entity_template('cell')
    cell_properties.set_type(cell, cell_type)
    cell_properties.set_position(cell, position)

    return cell


def setup_key_bindings():
    bindings = load_setting('key_bindings')
    return bindings


def load_entity_template(entity_type):
    return load_json_resource('entity_templates', entity_type)
