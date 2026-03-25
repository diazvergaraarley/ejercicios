# Schemas/player_schema.py
def create_player(name, player_class):
    base_stats = {
        "Warrior": {"hp": 120, "max hp": 120, "attack": 15, "defense": 10, "healing": 60, "exp": 0, "level": 1, "gold": 0},
        "Wizard": {"hp": 80, "max hp": 80, "attack": 20, "defense": 5, "healing": 40, "exp": 0, "level": 1, "gold": 0},
        "Archer": {"hp": 100,"max hp": 100, "attack": 12, "defense": 8, "healing": 50, "exp": 0, "level": 1, "gold": 0}
    }
    stats = base_stats.get(player_class, base_stats["Warrior"])
    
    player= {
        "current_zone": "village",
        "name" :name,
        "class": player_class,
        "hp": stats["hp"],
        "max_hp": stats["max hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "healing": stats["healing"],
        "exp": stats["exp"],
        "level": stats["level"],
        "gold": stats["gold"],
        "inventory": []
    }
    return player




































### def create_player(name, player_class):
###   base_stats = {
###       "Warrior": {"hp": 120, "attack": 15, "defense": 10},
###       "Wizard": {"hp": 80, "attack": 20, "defense": 5},
###       "Archer": {"hp": 100, "attack": 12, "defense": 8}
###   }
###
###   stats = base_stats.get(player_class, base_stats["Warrior"])
###
###   player = {
###       "name": name,
###       "class": player_class,
###       "hp": stats["hp"],
###       "max_hp": stats["hp"],
###       "attack": stats["attack"],
###       "defense": stats["defense"],
###       "level": 1,
###       "exp": 0,
###       "gold": 50,
###       "inventory": []
###   }
###
###   return player