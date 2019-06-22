import cell_fields
import character_fields
import character_fields as fields
import level_fields
from main import get_sign_for


def get_cell_at(level_data, position):
    x, y = position.values()
    return level_data[level_fields.CELLS][y][x]


def refresh_view(data, view):
    for cell in data[level_fields.UPDATES]:
        x, y = cell[cell_fields.POSITION].values()
        visitor = cell[cell_fields.VISITOR]
        if visitor:
            view[y][x] = get_sign_for(visitor[character_fields.TYPE])
        else:
            view[y][x] = get_sign_for(cell[cell_fields.TYPE])

    data[level_fields.UPDATES] = []


def update_visitor(level_data, position, visitor):
    cell = get_cell_at(level_data, position)
    cell[cell_fields.VISITOR] = visitor

    level_data[level_fields.UPDATES].append(cell)


def place_character(character, level_data):
    update_visitor(level_data, character[fields.POSITION], character)

    if character[fields.PREVIOUS_POSITION]:
        update_visitor(level_data, character[fields.PREVIOUS_POSITION], None)
