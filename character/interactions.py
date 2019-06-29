from character.character_actions import add_to_inventory, find_in_inventory
from item import item_types
from level import level_actions


def pick_up_item(character, item, level_data):
    add_to_inventory(character, item)
    level_actions.remove_item(level_data, item)


def try_opening_door(character, door, level_data):
    key = find_in_inventory(character, item_types.KEY)
    if key:
        level_actions.remove_obstacle(level_data, door)
