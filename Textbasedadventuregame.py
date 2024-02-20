def start_story():
    print("Welcome to the interactive story!")
    print("You find yourself in a dark forest. You hear a rustling sound nearby.")
    choice = input("Do you investigate the sound? (yes/no): ").lower()
    
    if choice == "yes":
        investigate_sound()
    elif choice == "no":
        print("You decide to stay put. Moments later, you hear footsteps approaching.")
        print("Game over.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        start_story()

def investigate_sound():
    print("You cautiously approach the source of the sound and discover a wounded animal.")
    choice = input("Do you try to help the animal? (yes/no): ").lower()
    
    if choice == "yes":
        help_animal()
    elif choice == "no":
        print("You decide to leave the animal alone and continue on your journey.")
        print("After a while, you stumble upon a hidden treasure!")
        print("Congratulations, you win!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        investigate_sound()

def help_animal():
    print("You bandage the animal's wound and it seems grateful.")
    choice = input("Do you continue to explore the forest or head back home? (explore/home): ").lower()
    
    if choice == "explore":
        print("You venture deeper into the forest and encounter a friendly wizard who grants you a wish!")
        print("Congratulations, you win!")
    elif choice == "home":
        print("You decide to head back home. On your way, you find a shortcut and reach home safely.")
        print("Game over.")
    else:
        print("Invalid choice. Please enter 'explore' or 'home'.")
        help_animal()

# Main function to start the story
start_story()
