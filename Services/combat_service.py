
def calculate_damage(attacker, defender):
    net_damage = max(attacker["attack"]-defender.get("defense", 0), 0)
    return net_damage

def player_attack(player, enemy):
    damage = calculate_damage(player, enemy)
    enemy["hp"] -= damage
    if enemy["hp"] < 0:
        enemy["hp"] = 0
    return enemy

def enemy_attack(enemy, player):
    damage = calculate_damage(enemy, player)
    player["hp"] -= damage
    if player["hp"] < 0:
        player["hp"] = 0 
    return player

def combat_turn(player, enemy, player_action):
    if player_action == "attack":
        enemy = player_attack(player, enemy)
    elif player_action == "defend":
        enemy_damage = calculate_damage(enemy, player) // 2
        player["hp"] -= enemy_damage
        if player["hp"] < 0:
            player["hp"] = 0
    elif player_action == "use_potion":
        pass  
    if enemy["hp"] > 0:
        player = enemy_attack(enemy, player)
    return player, enemy

def is_enemy_defeated(enemy):
    return enemy["hp"] <= 0

def combat_result(player, enemy):
    
    if enemy["hp"] <= 0:
        exp = enemy.get("exp_drop", 0)
        gold = enemy.get("gold_drop", 0)
        return exp, gold
    return 0, 0