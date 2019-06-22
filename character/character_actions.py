import copy

import cell_fields
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
    return target_cell[cell_fields.TYPE] in character[fields.WALKABLES]
