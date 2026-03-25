from Schemas.player_schema import create_player
from Services.world_service import get_next_enemy, advance_zone
from Services.combat_service import combat_turn, is_enemy_defeated, combat_result
from Services.player_service import gain_exp, earn_gold
from Services.inventory_service import show_inventory
from Data.zones_data import zones
from Data.enemies_data import enemies_stats

def create_character():
    name = input("Enter your character name: ")
    print(f"""\n
          Choose your class:
            1. Warrior
            2. Wizard
            3. Archer
          """
          )
    choice = (input("Select option: "))
    if choice == "1":
        player_class = "Warrior"
    elif choice == "2":
        player_class = "Wizard"
    elif choice == "3":
        player_class = "Archer"
    else:
        print("Invalid choice, defaulting to Warrior")
        player_class = "Warrior"
    player = create_player(name, player_class)
    return player
zones_order = ["village", "dark_forest", "cave", "castle"]
def start_game():
    player = create_character()
    
    print(f"\nWelcome {player['name']} the {player['class']}!")

    current_zone = player["current_zone"]
    defeated_enemies =[]
    running = True
    while running:
        enemy_name = get_next_enemy(current_zone, defeated_enemies, zones)
        if enemy_name is None:
            print(f"You cleared {current_zone}!")

            next_zone = advance_zone(current_zone, zones_order)

            if next_zone is None:
                print("You completed the game!")
                break

            current_zone = next_zone
            defeated_enemies = []
            print(f"Entering {current_zone}...")
            continue

 
        enemy = enemies_stats[enemy_name].copy()
        enemy["name"] = enemy_name
        print(f"\nYou encountered a {enemy_name}!")
        
        in_combat = True

        while in_combat:
            print(f"\nYou are in: {current_zone}\nFighting with: '{enemy_name}' ")
            
            print("\nChoose action:")
            print("1. Attack")
            print("2. Defend")
            print("3. Inventory")
            print("4. Exit")

            action = input("Option: ")
            if action == "1":
                player, enemy = combat_turn(player, enemy, "attack")
                print(f"Player HP: {player['hp']}")
                print(f"{enemy_name} HP: {enemy['hp']}")
            elif action == "2":
                player, enemy = combat_turn(player, enemy, "defend")
                print(f"Player HP: {player['hp']}")
                print(f"{enemy_name} HP: {enemy['hp']}")
            elif action == "3":
                show_inventory(player)
                continue
            elif action == "4":
                print("Exiting game...")
                running = False
                break
            else:
                print("Invalid option")
                continue
            if is_enemy_defeated(enemy):
                in_combat = False
                print(f"You defeated {enemy_name}!")
                exp, gold = combat_result(player, enemy)
                player, leveled_up = gain_exp(player, exp)
                player = earn_gold(player, gold)
                print(f"You gained {exp} EXP and {gold} gold")
                if leveled_up:
                    print(f" Congratulations! You reached level {player['level']}!")
                defeated_enemies.append(enemy_name)
                
            elif player["hp"] <= 0:
                print("You were defeated... but revived!")
                player["hp"] = player["max_hp"]
                in_combat = False
            if not running:
                in_combat = False
    