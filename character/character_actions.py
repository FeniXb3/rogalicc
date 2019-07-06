import copy

from data import data_loading
from interactable import interactable_actions, interactable_properties
from item import item_properties, item_types
from cell import cell_actions, cell_properties, cell_types
from character import character_fields as fields, entity_types, character_properties, interactions
from level import level_actions
from obstacle import obstacle_types, obstacle_properties
from position import position_actions


def move(character, target_position):
    set_previous_position_to_actual(character)
    character_properties.set_position(character, target_position)


def can_move(character, target_cell):
    obstacle = cell_properties.get_obstacle(target_cell)
    if obstacle:
        is_obstacle_walkable_action = obstacle_properties.get_is_walkable_action(obstacle)
        if not is_obstacle_walkable_action(obstacle):
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
    return item_properties.get_type(data) in character_properties.get_interactables(character)


def interact(character, target_cell, level_data):
    element = cell_actions.get_interactable_element(target_cell)
    element_type = item_properties.get_type(element)
    action = get_interaction_function(character, element_type)

    action(character, element, level_data)


def get_interaction_function(character, element_type):
    interactables = character_properties.get_interactables(character)
    interactable = interactables[element_type]
    return interactable_properties.get_interaction(interactable)


def add_interactable(character, interactable_type, interaction):
    interactables = character_properties.get_interactables(character)
    interactables[interactable_type] = interactable_actions.create_interactable(interaction)


def add_walkable(character, cell_type):
    character_properties.get_walkables(character).append(cell_type)


def set_previous_position_to_actual(character):
    character[fields.PREVIOUS_POSITION] = copy.deepcopy(character_properties.get_position(character))


def find_in_inventory(character, item_type):
    return next((item for item in character_properties.get_inventory(character) if item_properties.get_type(item) == item_type), None)


def create_player(get_action_name):
    player = data_loading.load_entity_template("character")
    character_properties.set_type(player, entity_types.PLAYER)
    character_properties.set_get_action_name(player, get_action_name)
    add_walkable(player, cell_types.STONE_FLOOR)
    add_interactable(player, item_types.KEY, interactions.pick_up_item)
    add_interactable(player, obstacle_types.DOOR, interactions.try_opening_door)

    return player


def try_interacting(character, level_data, target_cell):
    if can_interact(character, target_cell):
        interact(character, target_cell, level_data)


def perform_character_frame(character, directions, action_name, level_data):
    direction = directions[action_name]
    position = character_properties.get_position(character)
    target_position = position_actions.calculate_target_position(position, direction)
    target_cell = level_actions.get_cell_at(level_data, target_position)

    try_interacting(character, level_data, target_cell)
    if can_move(character, target_cell):
        move(character, target_position)
