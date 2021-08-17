from helpers import decision, killed_the_bees, saved_the_bees


# welcome_message function works
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
        "Do you check the oil or don't? (enter 'check' or 'don't')\n",
        "check", "don't", decision_four_step_back, decision_four_end)


# decision_four_step_back function works
def decision_four_step_back():
    """
    Back to second decision alternative, 'check' option
    redirects user to decision_five
    """
    print("\n.\n.\n.\n")
    print("You check the oil and it is very low")
    print("You decide to go back and take the bicycle instead")
    print("Can't risk it")
    print("\nBZzzzzzBzzzzzBzZZZ\n")
    print("Did you hear that? Anyway...")
    # decision_five function call, return to decision two 'bike'
    decision_five()


# decision_four_end function works
def decision_four_end():
    """
    Fourth decision ENDING, 'don't' option, game over
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


# decision_five function works
def decision_five():
    """
    Fifth decision function, 'bike' option
    """
    print("\n.\n.\n.\n")
    print("With no second guess, you hop on your bicycle")
    print("The weather is so good and you smell coffee around the corner")
    print("Even though you will be late you need some caffeine\n")
    # decision function call
    decision(
        "Do you stop for a coffee or go on? (enter 'stop' or 'go')\n",
        "stop", "go", decision_eight, decision_ten)


# decision_eight function works
def decision_eight():
    """
    Eighth decision function, 'stop' option
    """
    print("\n.\n.\n.\n")
    print("That coffee smells sooooo good")
    print("But the line is huge! It might take a while")
    print("And you forgot your reusable cup\n")
    # decision function call
    decision(
        "Do you wait in line or go? (enter 'wait' or 'go')\n",
        "wait", "go", decision_eight_end, decision_eight_step_back)


# decision_eight_step_back works
def decision_eight_step_back():
    """
    Back to fifth decision alternative, 'go' option
    redirects user to decision_ten
    """
    print("\n.\n.\n.\n")
    print("Just enjoy your ride and drink coffee at the office")
    print("What a beautiful day...")
    print("and you don't want to waste one more cup")
    print("\nBZzzzzzBzzzzzBzZZZ\n")
    print("What was that? Anyway...")
    # decision_ten function call, return to decision five 'go'
    decision_ten()


# decision_eight_end works
def decision_eight_end():
    """
    Eighth decision ENDING, 'wait' option, game over
    """
    print("'One cup won't make a difference', you think...")
    print("\n.\n.\n.\n")
    print("10 minutes later you are still waiting")
    print("You look behind and the line is huge")
    print("Everybody on their phones")
    print("One cloud in the blue sky catches your eye...\n")
    # killed_the_bees function call
    killed_the_bees(
        "What could you have done different?", start)


# decision_ten function works
def decision_ten():
    """
    Tenth decision function, 'go' option
    """
    print("\n.\n.\n.\n")
    print("Finally you have arrived at the building")
    print("Even though you enjoyed that ride your knees feel weak\n")
    # decision function call
    decision(
        "Hmmm, elevator or stairs? (enter 'elevator' or 'stairs')\n",
        "elevator", "stairs", decision_eleven, decision_ten_win)


# decision_ten_win works
def decision_ten_win():
    """
    Tenth decision function, 'stairs' option, saved_the_bees call
    """
    print("As you walk up the stairs you hear that noise again")
    print("\nBZzzzzzBzzzzzBzZZZ\n")
    print("The window is open and you go closer...")
    print("The sound becomes louder and louder and then you see her")
    print("The happiest bumblebee you've ever seen in your life!")
    # saved_the_bees function call
    saved_the_bees(start)


# decision_eleven function works
def decision_eleven():
    """
    Eleventh decision function, 'elevator' option
    """
    print("\n.\n.\n.\n")
    print("DING")
    print("You enter the elevator and hit the 7th floor")
    print("You hear somebody call 'Hold the door, hold the door!")
    print("There is nobody else in the elevator but you\n")
    # decision function call
    decision(
        "Do you hold the door or let it close? (enter 'hold' or 'close')\n",
        "hold", "close", decision_eleven_win, decision_eleven_end)


# TO DO: implement decision_eleven_win function
def decision_eleven_win():
    """
    Eleventh decision function, 'hold' option, saved_the_bees call
    """
    print("Test decision_eleven_win")


# TO DO: implement decision_eleven_end function
def decision_eleven_end():
    """
    Eleventh decision function, 'close' option, killed_the_bees call
    """
    print("Test decision_eleven_end")


start()
