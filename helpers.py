import time


# decision function call
def decision(user_input, first_option, second_option, path_one, path_two):
    """
    Decision function that checks for user input to match
    the required response and proceed to the next step
    """
    # check for user input to match first_option or second_option
    while True:
        option = input(user_input).lower()
        if option == first_option:
            print("\n.\n.\n.\n")
            # path_one function call (changes as story progresses)
            path_one()
            break
        elif option == second_option:
            print("\n.\n.\n.\n")
            # path_two function call (changes as story progresses)
            path_two()
            break
        else:
            # message to the user when input is not first or second option
            print(f"'{option}' is not a valid option.")
            print(f"Please enter '{first_option}' or '{second_option}'")
            continue


# killed_the_bees function call
def killed_the_bees(final_message, function):
    """
    Game over function
    """
    print(final_message)
    time.sleep(3)
    print("\n\n")
    print("                ###############################################")
    print("                #                                             #")
    print("                #              G A M E   O V E R              #")
    print("                #                                             #")
    print("                ###############################################")
    print("\n\n")
    # try_again function call
    play_again(function)


# saved_the_bees function call
def saved_the_bees(function):
    """
    Saved the bees function, end of game
    """
    time.sleep(3)
    print("\n\n")
    print("                ###############################################")
    print("                #                                             #")
    print("                #               Y      O      U               #")
    print("                #                S  A  V  E  D                #")
    print("                #                  T   H   E                  #")
    print("                #                   B E E S                   #")
    print("                #                      *                      #")
    print("                #                     / \                     #")
    print("                #                    /   \                    #")
    print("                #                   /     \                   #")
    print("                #                 _/       \_                 #")
    print("                #                                             #")
    print("                ###############################################")
    print("\n\n")
    # try_again function call
    play_again(function)


# try_again function call
def play_again(choice):
    """
    Try again function
    """
    print("Would you like to play again?")
    user_choice = input("(Type 'yes' or click the button to start over)\n")
    if user_choice.lower() == "yes":
        # choice function call > decision_one function call
        choice()
    else:
        print("See you next time!")


# print_statements function call
def print_statements(statements):
    for statement in statements:
        print(statement)
        time.sleep(1.5)
