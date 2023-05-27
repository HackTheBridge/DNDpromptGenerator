import random

def ask_number_of_players():
    while True:
        try:
            num_players = int(input("How many players? (1-4): "))
            if 1 <= num_players <= 4:
                return num_players
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_player_names(num_players):
    player_names = []
    for i in range(num_players):
        name = input(f"Enter the name of Player {i+1}: ")
        player_names.append(name)
    return player_names

def ask_game_rating():
    ratings = {
        'U': "The game rules are suitable for all ages. The vocabulary is very simple and the game play is basic enough for very young children. The game will require the player(s) to make simple 50:50 choices. The game will also require player(s) to roll a d6 to make the game more varied. 6 being a best and 1 being worst. There should be a crit bonus when 6s are rolled and the opposite when the a 1 is rolled. Include fights and combat as well as other actions. Provide a combination of player choices, storylines and dice rolls throughout the story.",
        'PG': "Parental guidance is suggested. Some content may not be suitable for young children.",
        '12': "Suitable for players aged 12 and above. Moderate level of violence or suggestive themes may be present.",
        '15': "Recommended for players aged 15 and above. Contains strong language, violence, or mature themes.",
        '18+': "For adult players only. Contains explicit content, violence, or intense themes."
    }
    while True:
        rating = input("Enter the game rating (U, PG, 12, 15, 18+): ")
        if rating in ratings:
            return rating, ratings[rating]
        else:
            print("Invalid rating. Please enter one of the given options.")

def choose_adventure():
    adventures = ['pirate', 'space', 'fantasy', 'dinosaur']
    print("Choose an adventure:")
    for i, adventure in enumerate(adventures, start=1):
        print(f"{i}. {adventure.capitalize()}")
    
    while True:
        try:
            choice = int(input("Enter the adventure number: "))
            if 1 <= choice <= len(adventures):
                return adventures[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the given options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_dm_props():
    props = input("Does the DM have any props they want to include? (Enter props separated by commas): ")
    props_list = [prop.strip() for prop in props.split(",")]
    return props_list

def main():
    num_players = ask_number_of_players()
    player_names = ask_player_names(num_players)
    game_rating, rating_rules = ask_game_rating()
    adventure = choose_adventure()
    dm_props = ask_dm_props()

    print("\n--- Game Summary ---")
    print(f"Number of players: {num_players}")
    print(f"Player names: {', '.join(player_names)}")
    print(f"Game rating: {game_rating}")
    print(f"Rating rules: {rating_rules}")
    print(f"Adventure: {adventure}")
    print(f"DM props: {', '.join(dm_props)}")

    print("\n--- Prompt ---")
    print(f"You act as the Dungeon Master and generate an adventure for the players based on player decisions.") 
    print(f"There will be {num_players} player(s) in this game.")
    print(f"The player(s) name(s) = {player_names}")
    print(f"The adventure will be {adventure} based. Please generate a {adventure} version of the player name(s).")
    print("Your job is generate the story so the DM can read out the adventure and guide the players. You can include lines for NPCs for the DM to read out but for any input you'll need to ask questions directly to the player(s).") 
    print("Any choices that the player makes for the adventure need to be numbered so the user can just enter a number to select their choice. Let players pick up items and remind them that they can use them in their choices.")
    print(f"The game rating is {game_rating}. The game rules are as follows:{rating_rules}.")
    if dm_props:
        print("Here are the DM props available:")
        for prop in dm_props:
            print(f"- {prop}")
        print("Feel free to incorporate these items into the story somewhere in the future.")

if __name__ == '__main__':
    main()
