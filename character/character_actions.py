import copy

from item import item_fields
from level import cell_fields
from character import character_fields as fields


def move(character, target_position):
    character[fields.PREVIOUS_POSITION] = copy.deepcopy(character[fields.POSITION])
    character[fields.POSITION] = copy.deepcopy(target_position)


def calculate_target_position(base_position, direction):
    target_position = {}

    for coord_key in direction:
        target_position[coord_key] = base_position[coord_key] + direction[coord_key]

    return target_position


def can_move(character, target_cell):
    obstacle = target_cell[cell_fields.OBSTACLE]
    if obstacle:
        return False

    return target_cell[cell_fields.TYPE] in character[fields.WALKABLES]


def add_to_inventory(character, item):
    inventory = character[fields.INVENTORY]
    inventory.append(item)


def can_interact(character, target_cell):
    return can_interact_with_item(character, target_cell) or can_interact_with_obstacle(character, target_cell)


def can_interact_with_item(character, target_cell):
    field = cell_fields.ITEM
    return can_interact_with_field(character, target_cell, field)


def can_interact_with_obstacle(character, target_cell):
    field = cell_fields.OBSTACLE
    return can_interact_with_field(character, target_cell, field)


def can_interact_with_field(character, target_cell, field):
    data = target_cell[field]
    if not data:
        return False

    return data[item_fields.TYPE] in character[fields.INTERACTABLES]


def get_interactable_element(cell):
    obstacle = cell[cell_fields.OBSTACLE]
    item = cell[cell_fields.ITEM]
    if obstacle:
        return obstacle
    if item:
        return item


def interact(character, target_cell, level_data):
    element = get_interactable_element(target_cell)
    element_type = element[item_fields.TYPE]
    action = character[fields.INTERACTABLES][element_type]

    action(character, element, level_data)


def set_name(character, name):
    character[fields.NAME] = name


def set_type(character, entity_type):
    character[fields.TYPE] = entity_type


def set_get_action_name(character, get_action_name_function):
    character[fields.GET_ACTION_NAME] = get_action_name_function


def set_position(character, position):
    character[fields.POSITION] = copy.deepcopy(position)


def add_interactable(character, interactable_type, interaction):
    character[fields.INTERACTABLES][interactable_type] = interaction


def add_walkable(character, cell_type):
    character[fields.WALKABLES].append(cell_type)


def get_get_action_name_function(character):
    return character[fields.GET_ACTION_NAME]


def get_position(character):
    return character[fields.POSITION]


def get_inventory(character):
    return character[fields.INVENTORY]
