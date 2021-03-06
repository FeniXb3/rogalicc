from cell import cell_properties
from character import character_properties
from item import item_actions, item_properties, item_parse_types
from level import level_fields
from data import signs, data_loading
from level import level_properties
from obstacle import obstacle_actions, obstacle_properties, obstacle_parse_types
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

    update_obstacle(level_data, position, door)


def add_key_to_level_at(level_data, x, y):
    position = position_actions.make_position(x, y)
    key_data = item_actions.create_key()
    item_properties.set_position(key_data, position)

    update_item(level_data, position, key_data)


def add_wall_to_level_at(level_data, x, y):
    position = position_actions.make_position(x, y)
    wall = obstacle_actions.create_wall()
    obstacle_properties.set_position(wall, position)

    update_obstacle(level_data, position, wall)


def get_adding_function_for(level_data, entity_type):
    return level_properties.get_adding_functions(level_data)[entity_type]


def add_adding_function(level_data, addable_type, adding_function):
    level_properties.get_adding_functions(level_data)[addable_type] = adding_function


def create_level():
    level_data = data_loading.load_entity_template('level')
    add_adding_function(level_data, obstacle_parse_types.WALL, add_wall_to_level_at)
    add_adding_function(level_data, obstacle_parse_types.DOOR, add_door_to_level_at)
    add_adding_function(level_data, obstacle_parse_types.LOCKED_DOOR, add_locked_door_to_level_at)
    add_adding_function(level_data, item_parse_types.KEY, add_key_to_level_at)

    return level_data


def add_locked_door_to_level_at(level_data, x, y):
    add_door_to_level_at(level_data, x, y, True)
