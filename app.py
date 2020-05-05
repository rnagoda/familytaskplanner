"""
Presents the user with the main menu

Allows the user to select an option and calls the appropriate methods

Tracks run_program to either continuously present the main menu or to quit executing the program
"""


import userActions as user_actions


def user_menu() -> bool:
    """
    Present the main menu options to the user, get the user's action selection and call appropriate functions

    :return: bool indicating whether to present the main menu again (True) or quit (False)
    """
    print("WHAT WOULD YOU LIKE TO DO:")
    print(" 1. See what projects exist")
    print(" 2. See which projects have been started")
    print(" 3. See which projects have been completed")
    print(" 4. Modify a project status")
    print(" 5. Add a new project.")
    print(" Q: Quit")
    user_action = input("")

    if user_action == '1':
        user_actions.projects_present_list_of_all()
    elif user_action == '2':
        user_actions.projects_present_list_of_all_started()
    elif user_action == 'q' or user_action == 'Q':
        print("Quitting App")
        return False
    else:
        print("Option Not Available - Stay Tuned ... ")

    print('\n\n\n')  # make room before presenting main menu options again
    return True


run_program = True
while run_program:
    run_program = user_menu()