from interactable import interactable_fields


def get_interaction(interactable):
    return interactable[interactable_fields.INTERACTION]


def get_condition(interactable):
    return interactable[interactable_fields.CONDITION]
