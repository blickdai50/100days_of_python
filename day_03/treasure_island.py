print('''
       ________________________________________________________
/  ____________________________________________________  \
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |_|___|___|___|___|___|___|___|___|___|___|___|___|__| |
|  ____________________________________________________  |
| | |   |   |   |   |   |   |   |   |   |   |   |   |  | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_| |
\___________________________________________________LGB__/
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

print("You're at a cross road. Where do you want to go?")
choice1 = input("    Type \"left\" or \"right\"\n")

if choice1 == "right":
    print("Fall into a hole.")
    print("Game Over.")
elif choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    choice2 = input("    Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if choice2 == "swim":
        print("Attacked by trout.")
        print("Game Over.")
    elif choice2 == "wait":
        print("You've come to a castle. There are three doors in the castle")
        choice3 = input("    Type \"red\" to open the red door, \"yellow\" for the yellow one, \"blue\" for the blue one .\n")
        if choice3 == "red":
            print("Burned by fire.")
            print("Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        elif choice3 == "blue":
            print("Eaten by beasts.")
            print("Game Over.")   