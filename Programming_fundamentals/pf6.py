def start():
    print("You are in a dark forest. There are two paths in front of you.")
    print("1. Take the left path")
    print("2. Take the right path")
    choice = input("What do you want to do? (1/2): ")
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start()

def left_path():
    print("You encounter a wild bear!")
    print("1. Fight the bear")
    print("2. Run away")
    choice = input("What do you want to do? (1/2): ")
    if choice == '1':
        fight_bear()
    elif choice == '2':
        run_away()
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("You find a treasure chest!")
    print("1. Open the chest")
    print("2. Leave it alone")
    choice = input("What do you want to do? (1/2): ")
    if choice == '1':
        open_chest()
    elif choice == '2':
        leave_chest()
    else:
        print("Invalid choice. Please try again.")
        right_path()

def fight_bear():
    print("You fought bravely, but the bear was too strong. You lost.")
    end_game()

def run_away():
    print("You ran away safely and found a hidden path to a village.")
    print("You win!")
    end_game()

def open_chest():
    print("The chest is filled with gold and jewels! You are rich!")
    print("You win!")
    end_game()

def leave_chest():
    print("You left the chest alone and walked away. However, you are curious about what was inside.")
    print("Game over.")
    end_game()

def end_game():
    print("Do you want to play again? (yes/no)")
    choice = input().lower()
    if choice == 'yes':
        start()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    start()
