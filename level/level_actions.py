from cell import cell_properties
from character import character_properties
from item import item_actions, item_properties
from level import level_fields
from data import signs
from level import level_properties
from obstacle import obstacle_actions, obstacle_properties, walkable_checks
from position import position_actions


def get_cell_at(level_data, position):
    x, y = position.values()
    return level_properties.get_cells(level_data)[y][x]


def clear_updates(level_data):
    level_data[level_fields.UPDATES] = []


def refresh_view(data, view):
    for cell in level_properties.get_updates(data):
        x, y = cell_properties.get_position(cell).values()
        visitor = cell_properties.get_visitor(cell)
        obstacle = cell_properties.get_obstacle(cell)
        item = cell_properties.get_item(cell)
        if visitor:
            view[y][x] = signs.get_character_sign_for(character_properties.get_type(visitor))
        elif obstacle:
            view[y][x] = signs.get_obstacle_sign_for(obstacle_properties.get_type(obstacle))
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
    position = obstacle_properties.get_position(obstacle)
    obstacle_actions.clear_position(obstacle)
    update_obstacle(level_data, position, None)


def add_door_to_level_at(level_data, x, y, is_locked=False):
    position = position_actions.make_position(x, y)
    door = obstacle_actions.create_door()
    obstacle_properties.set_position(door, position)
    obstacle_properties.set_is_locked(door, is_locked)
    obstacle_properties.set_is_walkable_action(door, walkable_checks.is_unlocked)

    update_obstacle(level_data, position, door)


def add_key_to_level_at(level_data, x, y):
    position = position_actions.make_position(x, y)
    key_data = item_actions.create_key()
    item_properties.set_position(key_data, position)

    update_item(level_data, position, key_data)
