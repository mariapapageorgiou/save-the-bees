def welcome_message():
    """
    Welcome function to print a message to the user
    """
    print()
    print("##############################################")
    print("#                                            #")
    print("#                    SAVE                    #")
    print("#                    THE                     #")
    print("#                    BEES                    #")
    print("#                                            #")
    print("#         Creator Maria Papageorgiou         #")
    print("#                                            #")
    print("##############################################\n\n")
    print("Add welcome message here\n")


def start():
    """
    Start function to retrieve username and start the game
    """
    welcome_message()

    # In order to esure that the user inputs a username use a while loop
    while True:
        USERNAME = input("Enter a username to begin your journey: \n")
        if USERNAME == "":
            print("Please enter a username to continue!\n")
            continue
        else:
            break
    print(f"\n{USERNAME}, your next steps will define the future of the bees!")
    print("Choose wisely...\n")  
    decision_one()


def decision_one():
    """
    First decision function, initial user decision
    """
    print("Monday morning, 8:07am... DING DING DING DING DING")
    print("You realize this is going to be the 3rd time you hit snooze.")
    print("You didn't get enough sleep last night...")
    # create a function to check for user input
    input("Do you hit snooze or get up? (enter 'snooze' or 'up')\n")


start()