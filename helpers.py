# decision function works
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


# TO DO: fix killed_the_bees function to take parameters of message and start
#        function
def killed_the_bees():
    """
    Game over function
    """
    print("Test functionality of 'killed_the_bees' function")
