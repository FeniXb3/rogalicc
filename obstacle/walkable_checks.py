from obstacle import obstacle_properties, obstacle_actions


def is_unlocked(obstacle):
    return not obstacle_properties.get_is_locked(obstacle)


def is_not_wall(obstacle):
    return not obstacle_actions.is_wall(obstacle)
