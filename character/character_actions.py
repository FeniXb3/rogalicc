import copy

from character import character_properties
from data import data_loading
from item import item_properties
from cell import cell_actions, cell_properties
from character import character_fields as fields, entity_types


def move(character, target_position):
    set_previous_position_to_actual(character)
    character_properties.set_position(character, target_position)


def can_move(character, target_cell):
    obstacle = cell_properties.get_obstacle(target_cell)
    if obstacle:
        return False

    return is_walkable(character, target_cell)


def is_walkable(character, target_cell):
    return cell_properties.get_type(target_cell) in character_properties.get_walkables(character)


def add_to_inventory(character, item):
    character_properties.get_inventory(character).append(item)


def can_interact(character, target_cell):
    return can_interact_with_item(character, target_cell) or can_interact_with_obstacle(character, target_cell)


def can_interact_with_item(character, target_cell):
    return can_interact_with_field(character, cell_properties.get_item, target_cell)


def can_interact_with_obstacle(character, target_cell):
    return can_interact_with_field(character, cell_properties.get_obstacle, target_cell)


def can_interact_with_field(character, get_action, cell):
    data = get_action(cell)
    if not data:
        return False

    return is_interactable(character, data)


def is_interactable(character, data):
    return item_properties.get_type(data) in get_interactables(character)


def interact(character, target_cell, level_data):
    element = cell_actions.get_interactable_element(target_cell)
    element_type = item_properties.get_type(element)
    action = get_interaction_function(character, element_type)

    action(character, element, level_data)


def get_interactables(character):
    return character[fields.INTERACTABLES]


def get_interaction_function(character, element_type):
    return get_interactables(character)[element_type]


def add_interactable(character, interactable_type, interaction):
    get_interactables(character)[interactable_type] = interaction


def add_walkable(character, cell_type):
    character_properties.get_walkables(character).append(cell_type)


def set_previous_position_to_actual(character):
    character[fields.PREVIOUS_POSITION] = copy.deepcopy(character_properties.get_position(character))


def find_in_inventory(character, item_type):
    return next((item for item in character_properties.get_inventory(character) if item_properties.get_type(item) == item_type), None)


def create_player():
    player = data_loading.load_entity_template("character")
    character_properties.set_type(player, entity_types.PLAYER)
    return player
