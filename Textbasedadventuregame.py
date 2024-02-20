def start_story():
    print("Welcome to the Haunted Mansion!")
    print("You find yourself standing in front of a spooky mansion.")
    print("Do you want to enter the mansion? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        enter_mansion()
    elif choice == "no":
        print("You decide not to enter the mansion and leave.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        start_story()

def enter_mansion():
    print("\nYou enter the mansion and the door slams shut behind you!")
    print("You are in a dimly lit foyer. There are two doors in front of you.")
    print("Do you want to go left or right? (left/right)")
    choice = input().lower()
    if choice == "left":
        explore_left_room()
    elif choice == "right":
        explore_right_room()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        enter_mansion()

def explore_left_room():
    print("\nYou enter a dusty library filled with cobwebs.")
    print("In the corner, you see a chest.")
    print("Do you want to open the chest? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print("You open the chest and find a key!")
        print("You take the key and leave the room.")
        enter_mansion()
    elif choice == "no":
        print("You decide not to open the chest and leave the room.")
        enter_mansion()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        explore_left_room()

def explore_right_room():
    print("\nYou enter a dark room with a single candle flickering on a table.")
    print("You hear strange noises coming from a closet in the corner.")
    print("Do you want to open the closet? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print("You open the closet and find a ghost!")
        print("The ghost scares you and you run out of the room.")
        enter_mansion()
    elif choice == "no":
        print("You decide not to open the closet and leave the room.")
        enter_mansion()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        explore_right_room()

start_story()
