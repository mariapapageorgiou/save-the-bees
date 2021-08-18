from helpers import decision, killed_the_bees, saved_the_bees, print_statements


# welcome_message function call
def welcome_message():
    """
    Welcome function to print a message to the user
    """
    print("                ##############################################")
    print("                #                                            #")
    print("                #                    SAVE                    #")
    print("                #                    THE                     #")
    print("                #                    BEES                    #")
    print("                #                                            #")
    print("                #         Creator Maria Papageorgiou         #")
    print("                #                                            #")
    print("                ##############################################")
    print_statements([
        "\n",
        "Fun Facts about bees:\n",
        "1. Bees beat their wings 11,400 times in one minute",
        "2. Only female bees can sting. Male bees don’t have stingers",
        "3. Honey bees communicate through a series of dance moves",
        "4. Each Honey Bee from the same hive has their own specific color",
        "   identification",
        "5. Bees have 5 eyes\n",
        "* * * Enjoy the game * * *\n"
    ])


# start function call
def start():
    """
    Start function to retrieve username and start the game
    """
    welcome_message()
    # In order to esure that the user inputs a username use a while loop
    while True:
        # global USERNAME in order to access the username input
        global USERNAME
        USERNAME = input("Enter a username to begin your journey: \n")
        if USERNAME == "":
            # promts the user to enter a username
            print("Please enter a username to continue!\n")
            continue
        else:
            break
    # print_statements function call
    print_statements([
        f"\n{USERNAME}, your next steps will define the future of the bees!",
        "Choose wisely...\n"
    ])
    # decision_one function call
    decision_one()


# decision_one function call
def decision_one():
    """
    First decision function, initial user decision
    """
    # print_statements function call
    print_statements([
        "\nMonday morning, 8:07am... DING DING DING DING",
        "You realize this is going to be the 3rd time you hit snooze.",
        "You didn't get enough sleep last night...\n"
    ])
    # decision function call
    decision(
        "Do you hit snooze or get up? (enter 'snooze' or 'up')\n",
        "snooze", "up", decision_two, decision_three)


# decision_two function call
def decision_two():
    """
    Second decision function, 'snooze' option
    """
    # print_statements function call
    print_statements([
        "Time goes by and the alarm goes off again... DING DING DING DING",
        "8:32am! You jump of the bed, get dressed quickly and out the door",
        "The office is only 15 minutes away on a bicycle,",
        "but you are very tired...\n"
    ])
    # decision function call
    decision(
        "Do you take the car or bike? (enter 'car' or 'bike')\n",
        "car", "bike", decision_four, decision_five)


# decision_three function call
def decision_three():
    """
    Third decision function, 'up' option
    """
    # print_statements function call
    print_statements([
        "'Aaaaaah', what a big yawn...",
        "You get up, put some music on and get dressed",
        "As you open the door to exit,",
        "you spot a few lights on at the end of the room\n"
    ])
    # decision function call
    decision(
        "Do you go back and turn them off or not? (enter 'off' or 'no')\n",
        "off", "no", decision_six, decision_seven)


# decision_four function call
def decision_four():
    """
    Fourth deicision function, 'car' option
    """
    # print_statements function call
    print_statements([
        "You get in the car and start the engine",
        "The oil indication is on\n"
    ])
    # decision function call
    decision(
        "Do you check the oil, yes or no? (enter 'yes' or 'no')\n",
        "yes", "no", decision_four_step_back, decision_four_end)


# decision_four_step_back function call
def decision_four_step_back():
    """
    Back to second decision alternative, 'yes' option
    redirects user to decision_five
    """
    # print_statements function call
    print_statements([
        "You check the oil and it is very low",
        "You decide to go back and take the bicycle instead",
        "Can't risk it",
        "\nBZzzzzzBzzzzzBzZZZ\n",
        "Did you hear that? Anyway..."
    ])
    # decision_five function call
    decision_five()


# decision_four_end function call
def decision_four_end():
    """
    Fourth decision ENDING, 'no' option, game over
    """
    # print_statements function call
    print_statements([
        "That light has been there a long time and never caused a problem\n",
        "3 minutes down the road, suddenly, you see smoke!",
        "Every second that passes more and more smoke appears",
        "The engine starts rumbling . . . and POUF",
        "Car is dead\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        "You look back on your decisions as a bee flies by...", decision_one)


# decision_five function call
def decision_five():
    """
    Fifth decision function, 'bike' option
    """
    # print_statements function call
    print_statements([
        "With no second guess, you hop on your bicycle",
        "The weather is so good and you smell coffee around the corner",
        "Even though you will be late you need some caffeine\n"
    ])
    # decision function call
    decision(
        "Do you stop for a coffee or go on? (enter 'stop' or 'go')\n",
        "stop", "go", decision_eight, decision_ten)


# decision_six function call
def decision_six():
    """
    Sixth decision function, 'off' option
    """
    # print_statements function call
    print_statements([
        "As you go down the stairs and look at your watch",
        "8:26am. Time has slipped by rather quickly",
        "You can make it on time if you walk",
        "But you don't want to rush at the same time\n"
    ])
    # decision function call
    decision(
        "Do you walk or take the car? (enter 'walk' or 'car')\n",
        "walk", "car", decision_nine, decision_four)


# decision_seven function call
def decision_seven():
    """
    Seventh decision function, 'no' option
    """
    # print_statements function call
    print_statements([
        "And out the door, down the elevator, out to the world",
        "The bus stop is only a block away",
        "Last time the bus was late and you didn't make it in time to work",
        "There is a taxi stopped at the traffic light\n"
    ])
    # decision function call
    decision(
        "Do you take the bus or taxi? (enter 'bus' or 'taxi')\n",
        "taxi", "bus", decision_seven_end, decision_twelve)


# decision_seven_end function call
def decision_seven_end():
    """
    Seventh decision function, 'taxi' option, game over
    """
    # print_statements function call
    print_statements([
        "'Taxi', you raise your hand",
        "The taxi accelerates very fast and stops right next to your feet",
        "As you open the door and enter you realize",
        "How filthy this taxi is\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        f"What do you think, {USERNAME}? Maybe walk next time?", decision_one)


# decision_eight function call
def decision_eight():
    """
    Eighth decision function, 'stop' option
    """
    # print_statements function call
    print_statements([
        "That coffee smells sooooo good",
        "But the line is huge! It might take a while",
        "And you forgot your reusable cup\n"
    ])
    # decision function call
    decision(
        "Do you wait in line or go? (enter 'wait' or 'go')\n",
        "wait", "go", decision_eight_end, decision_eight_step_back)


# decision_eight_step_back call
def decision_eight_step_back():
    """
    Back to fifth decision alternative, 'go' option
    redirects user to decision_ten
    """
    # print_statements function call
    print_statements([
        "Just enjoy your ride and drink coffee at the office",
        "What a beautiful day...",
        "and you don't want to waste one more cup",
        "\nBZzzzzzBzzzzzBzZZZ\n",
        "What was that? Anyway..."
    ])
    # decision_ten function call, return to decision five 'go'
    decision_ten()


# decision_eight_end call
def decision_eight_end():
    """
    Eighth decision ENDING, 'wait' option, game over
    """
    # print_statements function call
    print_statements([
        "'One cup won't make a difference', you think...\n.\n.\n.\n",
        "10 minutes later you are still waiting",
        "You look behind and the line is huge",
        "Everybody is on their phones",
        "In the background an overflowing trashcan catches your eye\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        f"One cup can make a difference after all, {USERNAME}!", decision_one)


# decision_nine function call
def decision_nine():
    """
    Ninth decision function, 'walk' option
    """
    # print_statements function call
    print_statements([
        "A few blocks the smell of fresh coffee burst through your nose",
        "You step over something and turn around to see what it was",
        "An empty plastic bottle on the ground\n"
    ])
    # decision function call
    decision(
        "Do youpick it up or keep on walking? (enter 'pick' or 'walk')\n",
        "pick", "walk", decision_ten, decision_nine_end)


# decision_nine_end function call
def decision_nine_end():
    """
    Ninth decision function, 'walk' option, game over
    """
    # print_statements function call
    print_statements([
        "'Somebody else will pick it up', you think",
        "There is a buzzing noise coming from behind",
        "You see the bee land on the plastic bottle\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        f"{USERNAME}, remember! Plastic takes up to 450 years to decompose.",
        decision_one)


# decision_ten function call
def decision_ten():
    """
    Tenth decision function, 'go' option
    """
    # print_statements function call
    print_statements([
        "Finally you have arrived at the building",
        "Your knees start to feel a bit weak\n"
    ])
    # decision function call
    decision(
        "Hmmm, elevator or stairs? (enter 'elevator' or 'stairs')\n",
        "elevator", "stairs", decision_eleven, decision_ten_win)


# decision_ten_alt function call
def decision_ten_alt():
    """
    Tenth alternative decision function, 'fruit' option
    """
    # print_statements function call
    print_statements([
        "'I will go for an apple and a banana, Pat. Don't need a bag'",
        "As you exit the shop, you hear something",
        "\nBZzzzzzBzzzzzBzZZZ\n\n.\n.\n.\n"
    ])
    # decision_ten function call
    decision_ten()


# decision_ten_win call
def decision_ten_win():
    """
    Tenth decision function, 'stairs' option, saved_the_bees call
    """
    # print_statements function call
    print_statements([
        "As you walk up the stairs you hear a noise",
        "\nBZzzzzzBzzzzzBzZZZ\n",
        "The window is open and you go closer...",
        "The sound becomes louder and louder and then you see her",
        "The happiest bumblebee you've ever seen in your life!"
    ])
    # saved_the_bees function call
    saved_the_bees(decision_one)


# decision_eleven function call
def decision_eleven():
    """
    Eleventh decision function, 'elevator' option
    """
    # print_statements function call
    print_statements([
        "DING\nYou enter the elevator and hit the 7th floor",
        "You hear somebody call 'Hold the door, hold the door!",
        "There is nobody else in the elevator but you\n"
    ])
    # decision function call
    decision(
        "Do you hold the door or let it close? (enter 'hold' or 'close')\n",
        "hold", "close", decision_eleven_win, decision_eleven_end)


# decision_eleven_win function call
def decision_eleven_win():
    """
    Eleventh decision function, 'hold' option, saved_the_bees call
    """
    # print_statements function call
    print_statements([
        "As you see the door close you hear a noise...",
        "\nBZzzzzzBzzzzzBzZZZ\n",
        "You raise your hand and stop the door the last minute",
        "A tiny little bee enters slowly and lands on your shoulder",
        f"'Oh thank you {USERNAME}', says your coworker out of breath",
        "You look at the curious bee . . .",
        "What a beautiful day"
    ])
    # saved_the_bees function call
    saved_the_bees(decision_one)


# decision_eleven_end function call
def decision_eleven_end():
    """
    Eleventh decision function, 'close' option, killed_the_bees call
    """
    # print_statements function call
    print_statements([
        "The elevator door closes\n",
        "Alone in the elevator, you listen...",
        "\nDING\n DING\n  DING\n   DING\n    DING\n     DING\n      DING\n",
        "As you come out, you see your coworker coming up the stairs",
        "'Sorry', you say.\nNo response\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        f"Maybe you should make a coffee and take it to them {USERNAME}?",
        decision_one)


# decision_twelve function call
def decision_twelve():
    """
    Twelfth decision function, 'bus' option
    """
    # print_statements function call
    print_statements([
        "You see it coming right around the corner",
        "'Great! I have time to stop for a snack'\n",
        "You get off the bus and enter the mini market next to your office",
        f"'Hey, {USERNAME}! How are you? I got your favorite sandwich in.'",
        "'Hi, Pat. Thank you, but I decided to be more considerate",
        "about prepackaged items and plastic waste'\n"
    ])
    # decision function call
    decision(
        "Do you go for a loose fruit or the prepackaged sandwich?"
        " (enter 'fruit' or 'sandwich')\n",
        "fruit", "sandwich", decision_ten_alt, decision_twelve_end)


# decision_twelve_end function call
def decision_twelve_end():
    """
    Twelfth end decision function, 'sandwich' option
    """
    # print_statements function call
    print_statements([
        "'Oh, it's ok, right?",
        "I will take the sandwich, Pat!'",
        "You unwrap it and a piece of the plastic flies up in the sky",
        "'Oh no!', you say.\n"
    ])
    # killed_the_bees function call
    killed_the_bees(
        f"Maybe you should make a coffee and take it to them {USERNAME}?",
        decision_one)


start()
