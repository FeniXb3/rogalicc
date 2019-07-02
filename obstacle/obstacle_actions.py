from data import data_loading
from obstacle import obstacle_fields, obstacle_types
from obstacle import obstacle_properties


def clear_position(obstacle):
    obstacle[obstacle_fields.POSITION] = None


def create_door():
    door = data_loading.load_entity_template('obstacle')
    obstacle_properties.set_type(door, obstacle_types.DOOR)
    return door


