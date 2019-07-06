from data import data_loading
from item import item_fields, item_types, item_properties


def clear_position(item):
    item[item_fields.POSITION] = None


def create_ring():
    ring = data_loading.load_entity_template('item')
    item_properties.set_type(ring, item_types.RING)
    return ring


def create_key():
    key = data_loading.load_entity_template('item')
    item_properties.set_type(key, item_types.KEY)
    return key


def get_position(item):
    return item[item_fields.POSITION]
