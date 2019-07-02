from cell import cell_properties


def get_interactable_element(cell):
    obstacle = cell_properties.get_obstacle(cell)
    item = cell_properties.get_item(cell)
    if obstacle:
        return obstacle
    if item:
        return item
