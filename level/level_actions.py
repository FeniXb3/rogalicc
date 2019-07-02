from cell import cell_properties
from character import character_properties
from item import item_actions, item_properties
from level import level_fields
from data import signs
from obstacle import obstacle_actions


def get_cell_at(level_data, position):
    x, y = position.values()
    return get_cells(level_data)[y][x]


def get_updates(level_data):
    return level_data[level_fields.UPDATES]


def clear_updates(level_data):
    level_data[level_fields.UPDATES] = []


def refresh_view(data, view):
    for cell in get_updates(data):
        x, y = cell_properties.get_position(cell).values()
        visitor = cell_properties.get_visitor(cell)
        obstacle = cell_properties.get_obstacle(cell)
        item = cell_properties.get_item(cell)
        if visitor:
            view[y][x] = signs.get_character_sign_for(character_properties.get_type(visitor))
        elif obstacle:
            view[y][x] = signs.get_obstacle_sign_for(obstacle_actions.get_type(obstacle))
        elif item:
            view[y][x] = signs.get_item_sign_for(item_properties.get_type(item))
        else:
            view[y][x] = signs.get_cell_sign_for(cell_properties.get_type(cell))

    clear_updates(data)


def update_visitor(level_data, position, visitor):
    update_cell_field(level_data, position, cell_properties.set_visitor, visitor)


def place_character(character, level_data):
    update_visitor(level_data, character_properties.get_position(character), character)

    previous_position = character_properties.get_previous_position(character)
    if previous_position:
        update_visitor(level_data, previous_position, None)


def update_item(level_data, position, item):
    update_cell_field(level_data, position, cell_properties.set_item, item)


def remove_item(level_data, item):
    position = item_properties.get_position(item)
    item_actions.clear_position(item)
    update_item(level_data, position, None)


def update_obstacle(level_data, position, obstacle):
    update_cell_field(level_data, position, cell_properties.set_obstacle, obstacle)


def update_cell_field(level_data, position, update_action, data):
    cell = get_cell_at(level_data, position)
    update_action(cell, data)
    queue_cell_update(level_data, cell)


def queue_cell_update(level_data, cell_data):
    level_data[level_fields.UPDATES].append(cell_data)


def remove_obstacle(level_data, obstacle):
    position = obstacle_actions.get_position(obstacle)
    obstacle_actions.clear_position(obstacle)
    update_obstacle(level_data, position, None)


def get_cells(level_data):
    return level_data[level_fields.CELLS]
