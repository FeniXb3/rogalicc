from level import level_fields, cell_fields
import position_fields as pos


def load_level():
    return [
        ['#','#','#','#','#','#','#','#','#','#','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','#','#','#','#','#','#','#','#','#','#']
    ]


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
        "player": "@",
        "empty": "."
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
                cell_fields.VISITOR: None
            }

            data_row.append(cell_data)

    return level_data


def get_sign_for(entity_type):
    signs = load_signs()

    return signs[entity_type]
