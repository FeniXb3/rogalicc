from obstacle import obstacle_properties


def is_unlocked(obstacle):
    return not obstacle_properties.get_is_locked(obstacle)
