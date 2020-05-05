import resources.dbDataProvider as db_actions


def projects_present_list_of_all():
    """
    Displays list of all existing projects
    """
    projects_print_list_pretty(db_actions.get_list_of_projects())


def projects_present_list_of_all_started():
    """
    Displays list of all existing projects with a status of 'started'
    """
    projects_print_list_pretty(db_actions.get_list_of_projects_status_started())


def projects_print_list_pretty(project_list):
    """
    Takes a list of projects and prints it in a friendly format
    """

    # Query DB for status values so that the status can be presented with the project
    status_list = db_actions.get_list_of_statuses()
    project_statuses = {}
    for status in status_list:
        project_statuses[status[0]] = status[1]

    for project in project_list:
        project_status = project_statuses[project[2]]
        print(f'Project: {project[1]}, status is: {project_status}')