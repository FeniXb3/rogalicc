import copy

from cell import cell_fields


def set_position(cell, position):
    cell[cell_fields.POSITION] = copy.deepcopy(position)


def set_type(cell, cell_type):
    cell[cell_fields.TYPE] = cell_type


def set_visitor(cell, visitor):
    cell[cell_fields.VISITOR] = visitor


def set_obstacle(cell, obstacle):
    cell[cell_fields.OBSTACLE] = obstacle


def set_item(cell, item):
    cell[cell_fields.ITEM] = item


def get_item(cell):
    return cell[cell_fields.ITEM]


def get_obstacle(cell):
    return cell[cell_fields.OBSTACLE]


def get_visitor(cell):
    return cell[cell_fields.VISITOR]


def get_position(cell):
    return cell[cell_fields.POSITION]


def get_type(cell):
    return cell[cell_fields.TYPE]
