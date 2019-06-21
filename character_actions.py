import character_fields as fields


def move(character, direction):
    for coord_key in direction:
        character[fields.PREVIOUS_POSITION][coord_key] = character[fields.POSITION][coord_key]
        character[fields.POSITION][coord_key] += direction[coord_key]
