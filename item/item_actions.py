from data import data_loading
from item import item_fields, item_types


def clear_position(item):
    item[item_fields.POSITION] = None


def get_position(item):
    return item[item_fields.POSITION]


def get_type(item):
    return item[item_fields.TYPE]


def set_type(item, item_type):
    item[item_fields.TYPE] = item_type


def set_position(item, position):
    item[item_fields.POSITION] = position


def create_ring():
    ring = data_loading.load_entity_template('item')
    set_type(ring, item_types.RING)
    return ring


def create_key():
    key = data_loading.load_entity_template('item')
    set_type(key, item_types.KEY)
    return key
