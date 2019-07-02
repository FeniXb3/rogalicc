from item import item_fields


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
