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
