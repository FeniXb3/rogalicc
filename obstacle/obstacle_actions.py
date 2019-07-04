from data import data_loading
from obstacle import obstacle_fields, obstacle_types
from obstacle import obstacle_properties


def clear_position(obstacle):
    obstacle[obstacle_fields.POSITION] = None


def create_door():
    door = data_loading.load_entity_template('obstacle')
    obstacle_properties.set_type(door, obstacle_types.DOOR)
    return door


def create_wall():
    wall = data_loading.load_entity_template('obstacle')
    obstacle_properties.set_type(wall, obstacle_types.WALL)
    return wall


def is_wall(obstacle):
    return obstacle_properties.get_type(obstacle) == obstacle_types.WALL
