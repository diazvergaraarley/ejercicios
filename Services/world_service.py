def get_next_enemy(current_zone, defeated_enemies, zones):
    enemies_in_zone = zones.get(current_zone, [])
    for enemy in enemies_in_zone:
        if enemy not in defeated_enemies:
            return enemy
    return None
def advance_zone(current_zone, zones_order):
    current_index= zones_order.index(current_zone)
    try:
        next_zone = zones_order[current_index + 1]
        return next_zone
    except ValueError:
        print(f"Error: {current_zone} not encountered in zones_order")
        return None