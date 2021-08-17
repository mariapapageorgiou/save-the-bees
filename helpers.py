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
    # TO DO: add try_again function to work here
    try_again(function)


# try_again function works
def try_again(choice):
    """
    Try again function
    """
    print("Would you like to try again and save the bees?")
    user_choice = input("(Type 'yes' or click the button to start over)\n")
    if user_choice == "yes":
        choice()
    else:
        print("See you next time...")
