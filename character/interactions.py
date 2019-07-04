from character import character_actions
from item import item_types
from level import level_actions
from obstacle import obstacle_properties


def pick_up_item(character, item, level_data):
    character_actions.add_to_inventory(character, item)
    level_actions.remove_item(level_data, item)


def try_opening_door(character, door, level_data):
    key = character_actions.find_in_inventory(character, item_types.KEY)
    if key:
        obstacle_properties.set_is_locked(door, False)
