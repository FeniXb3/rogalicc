import copy

from cell import cell_fields


def get_type(cell):
    return cell[cell_fields.TYPE]


def get_position(cell):
    return cell[cell_fields.POSITION]


def get_visitor(cell):
    return cell[cell_fields.VISITOR]


def get_obstacle(cell):
    return cell[cell_fields.OBSTACLE]


def get_item(cell):
    return cell[cell_fields.ITEM]


def set_item(cell, item):
    cell[cell_fields.ITEM] = item


def set_obstacle(cell, obstacle):
    cell[cell_fields.OBSTACLE] = obstacle


def set_visitor(cell, visitor):
    cell[cell_fields.VISITOR] = visitor


def set_type(cell, cell_type):
    cell[cell_fields.TYPE] = cell_type


def set_position(cell, position):
    cell[cell_fields.POSITION] = copy.deepcopy(position)


def get_interactable_element(cell):
    obstacle = get_obstacle(cell)
    item = get_item(cell)
    if obstacle:
        return obstacle
    if item:
        return item
