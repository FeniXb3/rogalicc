from interactable import interactable_fields


def create_interactable(interaction):
    interactable = {
        interactable_fields.INTERACTION: interaction
    }

    return interactable
