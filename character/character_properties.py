import copy

from character import character_fields as fields


def set_name(character, name):
    character[fields.NAME] = name


def set_type(character, entity_type):
    character[fields.TYPE] = entity_type


def set_get_action_name(character, get_action_name_function):
    character[fields.GET_ACTION_NAME] = get_action_name_function


def set_position(character, position):
    character[fields.POSITION] = copy.deepcopy(position)


def get_get_action_name_function(character):
    return character[fields.GET_ACTION_NAME]


def get_position(character):
    return character[fields.POSITION]


def get_inventory(character):
    return character[fields.INVENTORY]


def get_previous_position(character):
    return character[fields.PREVIOUS_POSITION]


def get_type(character):
    return character[fields.TYPE]


def get_walkables(character):
    return character[fields.WALKABLES]
