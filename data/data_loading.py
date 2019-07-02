import json
from queue import Queue

from character import entity_types
from character import action_names
from item import item_types
from level import position_fields as pos, level_actions
from cell import cell_types, cell_actions
from obstacle import obstacle_types


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
    setting_path = f'resources/settings/{setting_name}.json'
    with open(setting_path) as f:
        setting = json.load(f)

    return setting


def setup_directions():
    directions = load_setting('directions')

    return directions


def load_signs():
    signs = {
        entity_types.PLAYER: "@",
        cell_types.STONE_FLOOR: ".",
        cell_types.WALL: "#",
    }

    return signs


def get_cell_type_by_sign(cell_sign):
    for cell_type, sign in load_signs().items():
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


def get_sign_for(entity_type):
    signs = load_signs()

    return signs[entity_type]


def load_item_signs():
    signs = {
        item_types.KEY: "k"
    }

    return signs


def get_item_sign_for(item_type):
    signs = load_item_signs()

    return signs[item_type]


def load_obstacle_signs():
    signs = {
        obstacle_types.DOOR: "+"
    }

    return signs


def get_obstacle_sign_for(obstacle_type):
    signs = load_obstacle_signs()

    return signs[obstacle_type]


def setup_key_bindings():
    bindings = load_setting('key_bindings')
    return bindings


def load_entity_template(entity_type):
    template_path = 'resources/entity_templates/{entity_type}_template.json'.format(entity_type=entity_type)
    with open(template_path) as f:
        template = json.load(f)

    return template
