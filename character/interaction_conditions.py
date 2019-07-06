from character import character_properties
from item import item_actions


def default_interaction_condition(character, item):
    return True


def is_the_same_cell(character, item):
    return character_properties.get_position(character) == item_actions.get_position(item)
