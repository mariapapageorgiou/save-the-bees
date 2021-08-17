from helpers import decision, killed_the_bees


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
    # TO DO: Add welcome message
    print("Add welcome message here\n")


# start function works
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


# decision_one function works
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


# decision_two function works
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


# TO DO: implement decision_three function
def decision_three():
    """
    Third decision function, 'up' option
    """
    print("Test to check for decision function functionality")


# decision_four function works
def decision_four():
    """
    Fourth deicision function, 'car' option
    """
    print("\n.\n.\n.\n")
    print("You get in the car and start the engine.")
    print("The oil indication is on (and it has been on for a long time)")
    # decision function call
    decision(
        "Do you check the oil or don't? (enter 'check' or don't)\n",
        "check", "don't", decision_four_step_back, decision_four_end)


# decision_four_step_back function works
def decision_four_step_back():
    """
    Second decision alternative, 'check' option
    redirects user to decision_five
    """
    print("\n.\n.\n.\n")
    print("You check the oil and it is very low")
    print("You decide to go back and take the bicycle instead")
    print("Can't risk it")
    # decision_five function call, return to decision two 'bike'
    decision_five()


# decision_four_end function works
def decision_four_end():
    """
    Fourth decision ENDING, killed_the_bees
    """
    print("Aaah, there is no time to check the oil")
    print("\n.\n.\n.\n")
    print("3 minutes down the road, suddenly, you see smoke!")
    print("Every second that passes more and more smoke appears")
    print("The engine starts rumbling . . . and POUF")
    print("Car is dead")
    # killed_the_bees function call
    killed_the_bees(
        "You look back on your decisions as a bee flies by...", start)


# TO DO: implement decision_five function
def decision_five():
    """
    Fifth decision function, 'bike' option
    """
    print("Test decision_five function")


start()
