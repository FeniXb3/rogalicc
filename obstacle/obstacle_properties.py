import copy

from obstacle import obstacle_fields


def get_type(obstacle):
    return obstacle[obstacle_fields.TYPE]


def get_position(obstacle):
    return obstacle[obstacle_fields.POSITION]


def set_type(obstacle, obstacle_type):
    obstacle[obstacle_fields.TYPE] = obstacle_type


def set_position(obstacle, position):
    obstacle[obstacle_fields.POSITION] = copy.deepcopy(position)
