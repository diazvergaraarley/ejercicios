# player_service.py

def gain_exp(player, exp):
    player["exp"] += exp
    leveled_up = False               
    while player["exp"] >= 100:
        player["exp"] -= 100
        player["level"] += 1
        player["max_hp"] += 15
        player["attack"] += 10
        player["defense"] += 7
        player["hp"] = player["max_hp"]
        leveled_up = True             
    return player, leveled_up 

def use_potion(player, potion):
    if potion["type"] == "heal":
        player["hp"] += potion["amount"]  
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
    return player

def earn_gold(player, amount):
    player["gold"] += amount
    return player
def take_damage(player,damage):
    net_damage = max(damage - player["defense], 0"])
    player["hp"] -=net_damage
    if player["hp"] <0:
        player["hp"] = 0
    return player
