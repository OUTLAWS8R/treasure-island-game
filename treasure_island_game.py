import time
import sys

def start_game():
    while True:
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")
        
        while True:
            user_input = input("Choose Left or Right: ").strip().lower()
            if user_input == "left":
                print("You chose Left!")
                print("You fall into a hole.\nGame Over.")
                break
            elif user_input == "right":
                print("You chose Right!")
                print("There's a lake, an island in the center.")
                
                while True:
                    user_input = input("Do you want to swim to the island or do you want to wait? ").strip().lower()
                    if user_input == "wait":
                        print("You were attacked by Murlocs! Game Over!")
                        break
                    elif user_input == "swim":
                        print("You arrived at the island.\nThere's a small house nearby with 3 doors.\nYou arrive at the house.")
                        while True:
                            door_choice = input("There are 3 doors, which one will you choose? Red, Blue, or Yellow: ").strip().lower()
                            if door_choice == "red":
                                print("You were teleported back to the town. Please start again.")
                                break
                            elif door_choice == "yellow":
                                print("You found the Treasure! You Win!")
                                break
                            elif door_choice == "blue":
                                print("You were ambushed inside the house. Game Over!")
                                break
                            else:
                                print("Invalid choice. Please choose Red, Blue, or Yellow.")
                        break
                    else:
                        print("Invalid choice. Please choose to swim or wait.")
                break
            else:
                print("Invalid choice. Please choose Left or Right.")
        
        play_again = input("Would you like to play again or quit? (play/quit): ").strip().lower()
        if play_again == 'quit':
            print("Thanks for playing, Goodbye!")
            print("The game will close in 3, 2, 1...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            sys.exit()
        elif play_again != 'play':
            print("Invalid choice. Please choose play or quit.")
        else:
            print("Starting a new game...")
start_game()