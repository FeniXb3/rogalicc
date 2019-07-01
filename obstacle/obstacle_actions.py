from obstacle import obstacle_fields


def get_type(obstacle):
    return obstacle[obstacle_fields.TYPE]


def get_position(obstacle):
    return obstacle[obstacle_fields.POSITION]


def clear_position(obstacle):
    obstacle[obstacle_fields.POSITION] = None
