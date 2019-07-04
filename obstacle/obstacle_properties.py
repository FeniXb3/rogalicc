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


def get_is_walkable_action(obstacle):
    return obstacle[obstacle_fields.IS_WALKABLE_ACTION]


def set_is_walkable_action(obstacle, is_walkable_action):
    obstacle[obstacle_fields.IS_WALKABLE_ACTION] = is_walkable_action


def get_is_locked(obstacle):
    return obstacle[obstacle_fields.IS_LOCKED]


def set_is_locked(obstacle, is_locked):
    obstacle[obstacle_fields.IS_LOCKED] = is_locked
