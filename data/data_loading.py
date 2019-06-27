from character import entity_types
from item import item_types
from level import level_fields, cell_fields, position_fields as pos, cell_types


def load_level():
    basic_view = []
    with open('resources/levels/basic_level.rll') as f:
        for line in f:
            row = list(line.strip())
            basic_view.append(row)

    return basic_view


def setup_directions():
    directions = {
        "w": {
            pos.X: 0,
            pos.Y: -1
        },
        "s": {
            pos.X: 0,
            pos.Y: 1
        },
        "a": {
            pos.X: -1,
            pos.Y: 0
        },
        "d": {
            pos.X: 1,
            pos.Y: 0
        },
    }

    return directions


def load_signs():
    signs = {
        entity_types.PLAYER: "@",
        cell_types.EMPTY: ".",
    }

    return signs


def get_cell_type_by_sign(cell_sign):
    for cell_type, sign in load_signs().items():
        if sign == cell_sign:
            return cell_type


def parse_level_data(level_view):
    level_data = {
        level_fields.CELLS: [],
        level_fields.UPDATES: []
    }

    for y, row in enumerate(level_view):
        data_row = []
        level_data[level_fields.CELLS].append(data_row)
        for x, cell in enumerate(row):
            cell_type = get_cell_type_by_sign(cell)

            cell_data = {
                cell_fields.TYPE: cell_type,
                cell_fields.POSITION: {
                    pos.X: x,
                    pos.Y: y
                },
                cell_fields.VISITOR: None,
                cell_fields.ITEM: None
            }

            data_row.append(cell_data)

    return level_data


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
