import json

from character import entity_types
from character import action_names
from item import item_types
from level import level_fields, cell_fields, position_fields as pos, cell_types, level_actions
from obstacle import obstacle_types


def load_level():
    basic_view = []
    with open('resources/levels/basic_level.rll') as f:
        for line in f:
            row = list(line.strip())
            basic_view.append(row)

    return basic_view


def setup_directions():
    directions = {
        action_names.UP: {
            pos.X: 0,
            pos.Y: -1
        },
        action_names.DOWN: {
            pos.X: 0,
            pos.Y: 1
        },
        action_names.LEFT: {
            pos.X: -1,
            pos.Y: 0
        },
        action_names.RIGHT: {
            pos.X: 1,
            pos.Y: 0
        },
    }

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
    level_data = {
        level_fields.CELLS: [],
        level_fields.UPDATES: []
    }
    level_view = []

    for y, row in enumerate(level_raw_view):
        data_row = []
        level_data[level_fields.CELLS].append(data_row)
        view_row = []
        level_view.append(view_row)
        for x, cell in enumerate(row):
            cell_data = parse_cell(cell, x, y)
            data_row.append(cell_data)
            view_row.append(None)
            level_actions.queue_cell_update(level_data, cell_data)

    return level_data, level_view


def parse_cell(cell, x, y):
    cell_type = get_cell_type_by_sign(cell)
    cell_data = {
        cell_fields.TYPE: cell_type,
        cell_fields.POSITION: {
            pos.X: x,
            pos.Y: y
        },
        cell_fields.VISITOR: None,
        cell_fields.ITEM: None,
        cell_fields.OBSTACLE: None
    }
    return cell_data


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
    bindings = {
        "w": action_names.UP,
        "s": action_names.DOWN,
        "a": action_names.LEFT,
        "d": action_names.RIGHT,
        "q": action_names.QUIT
    }
    return bindings


def load_entity_template(entity_type):
    template_path = 'resources/entity_templates/{entity_type}_template.json'.format(entity_type=entity_type)
    with open(template_path) as f:
        template = json.load(f)

    return template
