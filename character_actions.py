import cell_fields
import character_fields as fields


def move(character, target_position):
    for coord_key in target_position:
        character[fields.PREVIOUS_POSITION][coord_key] = character[fields.POSITION][coord_key]
        character[fields.POSITION][coord_key] = target_position[coord_key]


def calculate_target_position(base_position, direction):
    target_position = {}

    for coord_key in direction:
        target_position[coord_key] = base_position[coord_key] + direction[coord_key]

    return target_position


def can_move(character, target_cell):
    return target_cell[cell_fields.TYPE] in character[fields.WALKABLES]
