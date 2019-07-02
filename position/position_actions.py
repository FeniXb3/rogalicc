from position import position_fields


def make_position(x, y):
    return {
        position_fields.X: x,
        position_fields.Y: y
    }


def calculate_target_position(base_position, direction):
    target_position = {}

    for coord_key in direction:
        target_position[coord_key] = base_position[coord_key] + direction[coord_key]

    return target_position
