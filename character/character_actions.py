import copy

from item import item_fields
from level import cell_fields, level_actions
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
    item = target_cell[cell_fields.ITEM]
    if not item:
        return False

    return item[item_fields.TYPE] in character[fields.INTERACTABLES]


def interact(character, target_cell, level_data):
    item = target_cell[cell_fields.ITEM]
    item_type = item[item_fields.TYPE]
    action = character[fields.INTERACTABLES][item_type]

    action(character, item, level_data)


def pick_up_item(character, item, level_data):
    add_to_inventory(character, item)
    level_actions.remove_item(level_data, item)
