import copy

from item import item_actions
from cell import cell_actions
from character import character_fields as fields


def move(character, target_position):
    set_previous_position_to_actual(character)
    set_position(character, target_position)


def calculate_target_position(base_position, direction):
    target_position = {}

    for coord_key in direction:
        target_position[coord_key] = base_position[coord_key] + direction[coord_key]

    return target_position


def can_move(character, target_cell):
    obstacle = cell_actions.get_obstacle(target_cell)
    if obstacle:
        return False

    return is_walkable(character, target_cell)


def is_walkable(character, target_cell):
    return cell_actions.get_type(target_cell) in character[fields.WALKABLES]


def add_to_inventory(character, item):
    inventory = character[fields.INVENTORY]
    inventory.append(item)


def can_interact(character, target_cell):
    return can_interact_with_item(character, target_cell) or can_interact_with_obstacle(character, target_cell)


def can_interact_with_item(character, target_cell):
    return can_interact_with_field(character, cell_actions.get_item, target_cell)


def can_interact_with_obstacle(character, target_cell):
    return can_interact_with_field(character, cell_actions.get_obstacle, target_cell)


def can_interact_with_field(character, get_action, cell):
    data = get_action(cell)
    if not data:
        return False

    return is_interactable(character, data)


def is_interactable(character, data):
    return item_actions.get_type(data) in character[fields.INTERACTABLES]


def get_interactable_element(cell):
    obstacle = cell_actions.get_obstacle(cell)
    item = cell_actions.get_item(cell)
    if obstacle:
        return obstacle
    if item:
        return item


def interact(character, target_cell, level_data):
    element = get_interactable_element(target_cell)
    element_type = item_actions.get_type(element)
    action = get_interaction_function(character, element_type)

    action(character, element, level_data)


def get_interaction_function(character, element_type):
    return character[fields.INTERACTABLES][element_type]


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


def set_previous_position_to_actual(character):
    character[fields.PREVIOUS_POSITION] = copy.deepcopy(character[fields.POSITION])


def find_in_inventory(character, item_type):
    return next((item for item in character[fields.INVENTORY] if item_actions.get_type(item) == item_type), None)


def get_previous_position(character):
    return character[fields.PREVIOUS_POSITION]


def get_type(character):
    return character[fields.TYPE]
