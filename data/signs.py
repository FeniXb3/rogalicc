from cell import cell_types
from data import data_loading


def load_cell_signs():
    return load_signs('cell')


def load_character_signs():
    return load_signs('character')


def get_default_cell_type():
    return cell_types.STONE_FLOOR


def get_cell_type_by_sign(cell_sign):
    for cell_type, sign in load_cell_signs().items():
        if sign == cell_sign:
            return cell_type

    return get_default_cell_type()


def get_cell_sign_for(entity_type):
    signs = load_cell_signs()

    return signs[entity_type]


def load_item_signs():
    return load_signs('item')


def get_item_sign_for(item_type):
    signs = load_item_signs()

    return signs[item_type]


def load_obstacle_signs():
    return load_signs('obstacle')


def get_obstacle_sign_for(obstacle_type):
    signs = load_obstacle_signs()

    return signs[obstacle_type]


def get_character_sign_for(character_type):
    signs = load_character_signs()

    return signs[character_type]


def load_signs(signs_type):
    return data_loading.load_json_resource('signs', signs_type)


def get_obstacle_type_by_sign(obstacle_sign):
    for obstacle_type, sign in load_obstacle_signs().items():
        if sign == obstacle_sign:
            return obstacle_type


def get_item_type_by_sign(item_sign):
    for item_type, sign in load_item_signs().items():
        if sign == item_sign:
            return item_type
