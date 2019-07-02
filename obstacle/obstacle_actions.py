import copy

from data import data_loading
from obstacle import obstacle_fields, obstacle_types


def get_type(obstacle):
    return obstacle[obstacle_fields.TYPE]


def get_position(obstacle):
    return obstacle[obstacle_fields.POSITION]


def clear_position(obstacle):
    obstacle[obstacle_fields.POSITION] = None


def set_type(obstacle, obstacle_type):
    obstacle[obstacle_fields.TYPE] = obstacle_type


def create_door():
    door = data_loading.load_entity_template('obstacle')
    set_type(door, obstacle_types.DOOR)
    return door


def set_position(obstacle, position):
    obstacle[obstacle_fields.POSITION] = copy.deepcopy(position)
