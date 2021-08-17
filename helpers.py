# decision function works
def decision(user_input, first_option, second_option, path_one, path_two):
    """
    Decision function that checks for user input to match
    the required response and proceed to the next step
    """
    # check for user input to match first_option or second_option
    while True:
        option = input(user_input)
        if option == first_option:
            # path_one function call (changes as story progresses)
            path_one()
            break
        elif option == second_option:
            # path_two function call (changes as story progresses)
            path_two()
            break
        else:
            # message to the user when input is not first or second option
            print(f"'{option}' is not a valid option.")
            print(f"Please enter '{first_option}' or '{second_option}'")
            continue


# killed_the_bees function works
def killed_the_bees(final_message, function):
    """
    Game over function
    """
    print(final_message)
    print("\n")
    print("###############################################")
    print("#                                             #")
    print("#              THE BEES ARE DEAD              #")
    print("#              G A M E   O V E R              #")
    print("#                                             #")
    print("###############################################\n\n")
    # try_again function call
    try_again(function)


# try_again function works
def try_again(choice):
    """
    Try again function
    """
    print("Would you like to try again and save the bees?")
    user_choice = input("(Type 'yes' or click the button to start over)\n")
    if user_choice == "yes":
        # choice function call > start function
        choice()
    else:
        print("See you next time!")
