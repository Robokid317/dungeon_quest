import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary

        player_name= input("Enter your name: ")
        player_class= input("Enter your class (Knight, Rogue, Sorcerer): ")
        if player_class.lower() == "knight":
            health = 12
            inventory = ["Sword", "Shield"]
            name = "Sir " + player_name
        elif player_class.lower() == "rogue":
            health = 8
            inventory = ["Dagger", "Crossbow"]
            name = player_name + " of the Night"
        elif player_class.lower() == "sorcerer":
            health = 6
            inventory = ["Staff", "Spell of Fire"]
            name = player_name + " the Powerful"
        else:
            print("Invalid class selected. Please choose Knight, Rogue, or Sorcerer.")
            return setup_player()  # This will prompt again for a valid class
        
        player_stats = f"Your current health: {health}, Your inventory: {inventory}"

        print(f"Welcome {name} let's see what you're starting with! {player_stats}")

        return {
            "name": name,
            "health": health,
            "inventory": inventory
        }


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary
        treasures = {
            "Sword": 6,
            "Shield": 4,
            "Crossbow": 8,
            "Staff": 12,
            "Spell of Fire": 10,
            "Dagger": 3,
            "Potato of Wonder": 45,
            "Helm": 3,
            "Slingshot": 4,
            "Heavenly Light": 18

        }
        return treasures
    
    
    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_name (str): The current room name.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room name and the 4 menu options listed above

        print(f"You are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened

        traps = [
             "You angered a blight and took damage! Your health is now {health}", 
             "You fell in a pit and injured yourself! Your health is now {health}", 
             "A gnome was not living for your nosiness diva, she read you to filth. Your health is now {health}",
             "Oh no, you got a boo boo! Your health is now {health}"
                ]

        outcome = random.choice(["treasure", "trap"])
        random_traps = random.choice(traps)


        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You found a {item}! Great adventurer you now have {treasures[item]} mana!")
        elif outcome == "trap":
            player["health"] -= 2
            print(random_traps.format(health=player['health']))
        return player


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
       
        print(f"Health: {player['health']}")
        if player["inventory"]:
            print("Inventory: " + ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."
        total_value = sum(treasures[item] for item in player["inventory"] if item in treasures)
        print("\nGame Over! Here is your summary:")
        print(f"Final Health: {player['health']}")
        print(f"Items Collected: {', '.join(player['inventory']) if player['inventory'] else 'None'}")
        print(f"Total Value: {total_value}")
        total_score = sum(treasures[item] for item in player["inventory"] if item in treasures and player["health"] > 0)
        print(f"You have a total score of {total_score} points.")

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

        for room_number in range(1, 6):
            print(f"\n--- Entering Room {room_number} ---")
            while True:
                display_options(room_number)
                choice = input("Choose an option (1-4): ")
                
                if choice == "1":
                    player = search_room(player, treasures)
                    if player["health"] < 1:
                        print("You have run out of health!")
                        end_game(player, treasures)
                        return
                elif choice == "2":
                    print("Moving to the next room...")
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("Quitting the game...")
                    end_game(player, treasures)
                else:
                    print("Invalid choice. Please select a valid option.")


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
