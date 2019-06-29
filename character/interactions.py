from character import character_fields as fields
from character.character_actions import add_to_inventory
from item import item_fields, item_types
from level import level_actions


def pick_up_item(character, item, level_data):
    add_to_inventory(character, item)
    level_actions.remove_item(level_data, item)


def try_opening_door(character, door, level_data):
    key = next((item for item in character[fields.INVENTORY] if item[item_fields.TYPE] == item_types.KEY), None)
    if key:
        level_actions.remove_obstacle(level_data, door)
