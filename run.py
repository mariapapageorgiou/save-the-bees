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
            # promts the user to enter a username
            print("Please enter a username to continue!\n")
            continue
        else:
            break
    print(f"\n{USERNAME}, your next steps will define the future of the bees!")
    print("Choose wisely...\n")
    # decision_one function call
    decision_one()


def decision(user_input, first_option, second_option, path_one, path_two):
    """
    Decision function that checks for user input to match
    the required response and proceed to the next step
    """
    while True:
        option = input(user_input)
        if option == first_option:
            path_one()
            break
        elif option == second_option:
            path_two()
            break
        else:
            # message to the user when input is not first or second option
            print(f"'{option}' is not a valid option.")
            print(f"Please enter '{first_option}' or '{second_option}'")
            continue


def killed_the_bees():
    """
    Game over function
    """
    print("Test functionality of 'killed_the_bees' function")


def decision_one():
    """
    First decision function, initial user decision
    """
    print("Monday morning, 8:07am... DING DING DING DING")
    print("You realize this is going to be the 3rd time you hit snooze.")
    print("You didn't get enough sleep last night...\n")
    # decision function call
    decision(
        "Do you hit snooze or get up? (enter 'snooze' or 'up')\n",
        "snooze", "up", decision_two, decision_three)


def decision_two():
    """
    Second decision function, 'snooze' option
    """
    print("\n.\n.\n.\n")
    print("Time goes by and the alarm goes off again... DING DING DING DING")
    print("8:32am! You jump of the bed, get dressed quickly and out the door")
    print("The office is only 15 minutes away on a bicycle,")
    print("but you are very tired...\n")
    # decision function call
    decision(
        "Do you take the car or bike? (enter 'car' or 'bike')\n",
        "car", "bike", decision_four, decision_five)


def decision_three():
    """
    Third decision function, 'up' option
    """
    print("Test to check for decision function functionality")


def decision_four():
    """
    Fourth deicision function, 'car' option
    """
    print("\n.\n.\n.\n")
    print("You get in the car and start the engine.")
    print("The oil indication is on (and it has been on for a looooong time)")
    # decision function call
    decision(
        "Do you check the oil or don't? (enter 'check' or don't)\n",
        "check", "don't", decision_two_alternate, killed_the_bees)


def decision_five():
    """
    Fifth decision function, 'bike' option
    """
    print("Test to check for functionality")


def decision_two_alternate():
    """
    Second decision alternative, 'check' option
    redirects user to decision_five
    """
    print("You check the oil on the engine and it is very low")
    print("You decide to go back and take the bicycle instead")
    decision_five()


start()
