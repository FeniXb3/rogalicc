from level import level_fields


def get_cells(level_data):
    return level_data[level_fields.CELLS]


def get_updates(level_data):
    return level_data[level_fields.UPDATES]


def get_adding_functions(level_data):
    return level_data[level_fields.ADDING_FUNCTIONS]
