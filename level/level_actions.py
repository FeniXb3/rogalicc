from character import character_actions
from item import item_actions
from level import level_fields, cell_fields
from data import data_loading
from obstacle import obstacle_fields


def get_cell_at(level_data, position):
    x, y = position.values()
    return level_data[level_fields.CELLS][y][x]


def refresh_view(data, view):
    for cell in data[level_fields.UPDATES]:
        x, y = cell[cell_fields.POSITION].values()
        visitor = cell[cell_fields.VISITOR]
        obstacle = cell[cell_fields.OBSTACLE]
        item = cell[cell_fields.ITEM]
        if visitor:
            view[y][x] = data_loading.get_sign_for(character_actions.get_type(visitor))
        elif obstacle:
            view[y][x] = data_loading.get_obstacle_sign_for(obstacle[obstacle_fields.TYPE])
        elif item:
            view[y][x] = data_loading.get_item_sign_for(item_actions.get_type(item))
        else:
            view[y][x] = data_loading.get_sign_for(cell[cell_fields.TYPE])

    data[level_fields.UPDATES] = []


def update_visitor(level_data, position, visitor):
    field = cell_fields.VISITOR
    update_cell_field(level_data, position, field, visitor)


def place_character(character, level_data):
    update_visitor(level_data, character_actions.get_position(character), character)

    previous_position = character_actions.get_previous_position(character)
    if previous_position:
        update_visitor(level_data, previous_position, None)


def update_item(level_data, position, item):
    field = cell_fields.ITEM
    update_cell_field(level_data, position, field, item)


def remove_item(level_data, item):
    position = item_actions.get_position(item)
    item_actions.clear_position(item)
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


def remove_obstacle(level_data, obstacle):
    position = obstacle[obstacle_fields.POSITION]
    obstacle[obstacle_fields.POSITION] = None
    update_obstacle(level_data, position, None)
