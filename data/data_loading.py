import json
from queue import Queue

from level import position_fields as pos, level_actions
from cell import cell_actions


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


def load_signs(signs_type):
    return load_json_resource('signs', signs_type)


def load_cell_signs():
    return load_signs('cell')


def load_visitor_signs():
    return load_signs('character')


def get_cell_type_by_sign(cell_sign):
    for cell_type, sign in load_cell_signs().items():
        if sign == cell_sign:
            return cell_type


def parse_level_data(level_raw_view):
    level_data = load_entity_template('level')
    level_view = []

    for y, row in enumerate(level_raw_view):
        data_row = []
        level_actions.get_cells(level_data).append(data_row)
        view_row = []
        level_view.append(view_row)
        for x, cell in enumerate(row):
            cell_data = parse_cell(cell, x, y)
            data_row.append(cell_data)
            view_row.append(None)
            level_actions.queue_cell_update(level_data, cell_data)

    return level_data, level_view


def parse_cell(cell_sign, x, y):
    position = {
        pos.X: x,
        pos.Y: y
    }

    cell_type = get_cell_type_by_sign(cell_sign)
    cell = load_entity_template('cell')
    cell_actions.set_type(cell, cell_type)
    cell_actions.set_position(cell, position)

    return cell


def get_cell_sign_for(entity_type):
    signs = load_cell_signs()

    return signs[entity_type]


def load_item_signs():
    return load_signs('item')


def get_item_sign_for(item_type):
    signs = load_item_signs()

    return signs[item_type]


def load_obstacle_signs():
    return load_signs('obstacle')


def get_obstacle_sign_for(obstacle_type):
    signs = load_obstacle_signs()

    return signs[obstacle_type]


def setup_key_bindings():
    bindings = load_setting('key_bindings')
    return bindings


def load_entity_template(entity_type):
    return load_json_resource('entity_templates', entity_type)


def get_visitor_sign_for(visitor_type):
    signs = load_visitor_signs()

    return signs[visitor_type]
