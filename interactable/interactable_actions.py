from character import interaction_conditions
from interactable import interactable_fields


def create_interactable(interaction, condition):
    condition = condition if condition else interaction_conditions.default_interaction_condition

    interactable = {
        interactable_fields.CONDITION: condition,
        interactable_fields.INTERACTION: interaction
    }

    return interactable
