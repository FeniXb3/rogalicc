from character import character_fields, character_fields as fields
from item import item_fields
from level import level_fields, cell_fields
from data import data_loading


def get_cell_at(level_data, position):
    x, y = position.values()
    return level_data[level_fields.CELLS][y][x]


def refresh_view(data, view):
    for cell in data[level_fields.UPDATES]:
        x, y = cell[cell_fields.POSITION].values()
        visitor = cell[cell_fields.VISITOR]
        item = cell[cell_fields.ITEM]
        if visitor:
            view[y][x] = data_loading.get_sign_for(visitor[character_fields.TYPE])
        elif item:
            view[y][x] = data_loading.get_item_sign_for(item[item_fields.TYPE])
        else:
            view[y][x] = data_loading.get_sign_for(cell[cell_fields.TYPE])

    data[level_fields.UPDATES] = []


def update_visitor(level_data, position, visitor):
    field = cell_fields.VISITOR
    update_cell_field(level_data, position, field, visitor)


def place_character(character, level_data):
    update_visitor(level_data, character[fields.POSITION], character)

    if character[fields.PREVIOUS_POSITION]:
        update_visitor(level_data, character[fields.PREVIOUS_POSITION], None)


def update_item(level_data, position, item):
    field = cell_fields.ITEM
    update_cell_field(level_data, position, field, item)


def remove_item(level_data, item):
    position = item[item_fields.POSITION]
    item[item_fields.POSITION] = None
    update_item(level_data, position, None)


def update_obstacle(level_data, position, obstacle):
    field = cell_fields.OBSTACLE
    update_cell_field(level_data, position, field, obstacle)


def update_cell_field(level_data, position, field, data):
    cell = get_cell_at(level_data, position)
    cell[field] = data
    queue_cell_update(level_data, cell)


def queue_cell_update(level_data, cell_data):
    level_data[level_fields.UPDATES].append(cell_data)
