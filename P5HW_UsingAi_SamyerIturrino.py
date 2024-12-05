# Samyer Iturrino
# 12-3-24
# Character Creation Game
# Brief description of program: This program allows players to create characters with attributes like name, health, and attack points, display characters, and battle each other. The battle reduces health of the target character based on random damage.

import random

# 1. Value-returning function to create a character
def create_character():
    """Prompts the user to create a character and returns a dictionary of character attributes."""
    print("Let's create a new character!")
    name = input("Enter the character's name: ")
    health = int(input("Enter the character's health: "))
    attack_points = int(input("Enter the character's attack points: "))
    
    character = {
        'name': name,
        'health': health,
        'attack_points': attack_points
    }
    
    return character

# 2. Non-value returning function to display all characters
def display_characters(character_list):
    """Displays all characters' details."""
    print("\n--- Character List ---")
    if not character_list:
        print("No characters created yet!")
        return
    for i, character in enumerate(character_list):
        print(f"Character {i + 1}:")
        for key, value in character.items():
            print(f"{key.capitalize()}: {value}")
        print()

# 3. Game logic function for characters to battle
def battle(character1, character2):
    """Simulates a battle between two characters."""
    print(f"\nBattle between {character1['name']} and {character2['name']}!")
    
    # Random damage based on character's attack points
    damage = random.randint(1, character1['attack_points'])
    print(f"{character1['name']} attacks {character2['name']} and deals {damage} damage.")
    
    character2['health'] -= damage
    
    # Check if character2 has survived
    if character2['health'] <= 0:
        print(f"{character2['name']} has been defeated!")
    else:
        print(f"{character2['name']} now has {character2['health']} health.")
    
    return character1, character2

# 4. Main function that controls the flow of the game
def main():
    """Main function to run the game loop."""
    characters = []  # List to hold created characters
    
    while True:
        print("\n--- Game Menu ---")
        print("1. Create a character")
        print("2. Display all characters")
        print("3. Battle (Choose 2 characters to battle)")
        print("4. Exit the game")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            character = create_character()
            characters.append(character)
        
        elif choice == '2':
            display_characters(characters)
        
        elif choice == '3':
            if len(characters) < 2:
                print("You need at least two characters to battle!")
            else:
                # Select two characters to battle
                print("Choose two characters to battle:")
                for i, character in enumerate(characters):
                    print(f"{i + 1}. {character['name']}")
                
                first_choice = int(input("Choose the first character (1, 2, ...): ")) - 1
                second_choice = int(input("Choose the second character (1, 2, ...): ")) - 1
                
                # Ensure the second character isn't the same as the first
                while first_choice == second_choice:
                    print("You must choose two different characters.")
                    second_choice = int(input("Choose a different second character (1, 2, ...): ")) - 1
                
                # Perform battle
                character1 = characters[first_choice]
                character2 = characters[second_choice]
                
                characters[first_choice], characters[second_choice] = battle(character1, character2)
        
        elif choice == '4':
            print("Thank you for playing!")
            break
        
        else:
            print("Invalid choice. Please choose again.")

# Run the game
if __name__ == "__main__":
    main()
