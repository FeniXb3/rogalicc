from item import item_fields


def clear_position(item):

    item[item_fields.POSITION] = None


def get_position(item):
    return item[item_fields.POSITION]


def get_type(item):
    return item[item_fields.TYPE]
