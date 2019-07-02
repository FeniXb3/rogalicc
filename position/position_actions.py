from position import position_fields


def make_position(x, y):
    return {
        position_fields.X: x,
        position_fields.Y: y
    }
