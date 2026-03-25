
def add_item(player, item):
    player["inventory"].append(item)
    return player
def remove_item(player, item_name):
    player["inventory"] = [item for item in player["inventory"] if item["name"] != item_name]
    return player
def use_item(player, item_name):
    item_to_use= None
    for item in player["inventory"]:
        if item["name"] == item_name:
            item_to_use = item
            break       
        if item_to_use["type"] == "heal":
            player["hp"] += item_to_use["amount"]
            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]
        player = remove_item(player, item_name)
        return player

def list_inventory(player):
    return [item["name"] for item in player["inventory"]]

def show_inventory(player):
    print("\n--- Inventory ---")
    print("Gold:", player["gold"])
    print("EXP:", player["exp"])
    if player["inventory"]:
        for item in player["inventory"]:
            print("-", item["name"])
    else:
        print("Inventory empty")