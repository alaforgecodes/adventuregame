import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


def print_dramatic_pause(text):
    print(text)
    time.sleep(3)


def intro():
    print_dramatic_pause("You stand at the edge of a dark forest.")
    print_dramatic_pause("You've heard the monster terrorizing "
                         "the nearby town lives here.")
    print_dramatic_pause("You see that the path you followed "
                         "from town splits in two.")
    print_dramatic_pause("The path to the right leads to a "
                         "cave shaped like a dragon's skull.")
    print_dramatic_pause("The path to the left leads to a dark house.")
    print_dramatic_pause("In your pocket is a chipped butter knife.")
    print("")


def explore():
    print("")
    print_pause("What would you like to do?")
    print_pause("Enter 1 to explore the cave.")
    print_pause("Enter 2 to inspect the house.")
    print("")


def explore_cave(items, weapon, monster):
    print("")
    if weapon not in items:
        items.append(weapon)
        print_pause("You approach the cave.")
        print_pause("Sharp stones like fangs reach down toward you.")
        print_pause("In the faint light, something catches your eye.")
        print_pause("You step forward and pick up the object.")
        print_pause(f"You have obtained {weapon}.")
        print("")
    else:
        print_pause("The cave is empty. There is nothing else to do here.")
        print("")
    print_pause("You head back the way you came.")
    adventure(items, weapon, monster)


def explore_house(items, weapon, monster):
    print("")
    print_pause("You approach the house.")
    print_pause("No light shines from the windows.")
    print_pause("You listen but only hear the sound "
                "of the wind through the trees.")
    print_pause("You go to knock on the door when "
                "it swings open.")
    print_pause(f"A {monster} stands in the doorway!")
    print_pause("It roars and reaches toward you.")
    print("")
    flight_or_fight(items, weapon, monster)


def flight_or_fight(items, weapon, monster):
    print_pause("What do you do?")
    print_pause("Enter 1 to fight.")
    print_pause("Enter 2 to run away.")
    print("")
    choice = input("Please enter 1 or 2.\n")
    if choice == '1':
        combat(items, weapon, monster)
    elif choice == '2':
        flee(items, weapon, monster)
    else:
        print_pause("Invalid input. Please enter 1 or 2.")


def combat(items, weapon, monster):
    print("")
    if weapon in items:
        print_dramatic_pause(f"You brandish the {weapon}.")
        print_dramatic_pause(f"The {monster} roars.")
        print_dramatic_pause("You fight for what feels like eternity.")
        print_dramatic_pause(f"Finally, the {monster} falls "
                             "to the ground, defeated.")
        print_dramatic_pause("You have won the game!")
        play_again()
    else:
        print_dramatic_pause("You pull the chipped butter knife "
                             "from your pocket.")
        print_dramatic_pause(f"The {monster} roars. It knocks "
                             "the knife out of your hand.")
        print_dramatic_pause(f"As the {monster} lunges toward "
                             "you, you hope the end will be quick.")
        print_dramatic_pause("You have lost the game.")
        play_again()


def flee(items, weapon, monster):
    print("")
    print_pause("You turn and run back up the path.")
    print_pause("You here a roar and feel something grab "
                "for the back of your shirt, "
                "but you are able to escape.")
    adventure(items, weapon, monster)


def play_again():
    print("")
    again = input("Would you like to play again? y/n \n")
    if again == "y":
        play_game()
    elif again == "n":
        print_pause("Thank you for playing!")
    else:
        print_pause("Invalid input.")
        play_again()


def adventure(items, weapon, monster):
    explore()
    response = input("Please enter 1 or 2.\n")
    if response == '1':
        explore_cave(items, weapon, monster)
    elif response == '2':
        explore_house(items, weapon, monster)
    else:
        print_pause("Invalid input.")
        adventure(items, weapon, monster)


def play_game():
    items = []
    monsters = ["demon", "zombie", "vampire", "chimera", "minotaur"]
    weapons = ["glowing orb", "shining sword", "ancient amulet"]
    weapon = random.choice(weapons)
    monster = random.choice(monsters)
    intro()
    adventure(items, weapon, monster)


play_game()
