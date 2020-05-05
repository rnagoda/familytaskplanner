import resources.dbDataProvider as db_actions


def present_user_menu() -> bool:
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
        projects_present_list_of_all()
    elif user_action == '2':
        projects_present_list_of_status('started')
    elif user_action == '3':
        projects_present_list_of_status('complete')
    elif user_action == 'q' or user_action == 'Q':
        print("Quitting App")
        return False
    else:
        print("Option Not Available - Stay Tuned ... ")

    print('\n\n\n')  # make room before presenting main menu options again
    return True


def projects_present_list_of_all():
    """
    Displays list of all existing projects
    """
    projects_print_list_pretty(db_actions.get_list_of_projects())


def projects_present_list_of_status(status):
    """
    Displays list of all existing projects with a status of 'started'
    """
    projects_print_list_pretty(db_actions.get_list_of_projects_with_status(status))


def projects_print_list_pretty(project_list):
    """
    Takes a list of projects and prints it in a friendly format
    """

    project_statuses = db_actions.get_dict_of_statuses()  # Use this to show a friendly status name

    for project in project_list:
        project_status = project_statuses[project[2]]
        print(f'Project: {project[1]}\nStatus: {project_status}\n')