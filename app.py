from project import Project
from resources.dbDataProvider import get_list_of_projects

project_name = 'New Porch'

current_project = Project(project_name)

print(current_project)


def user_menu() -> bool:
    print("WHAT WOULD YOU LIKE TO DO:")
    print(" 1. See what projects exist")
    print(" 2. See which projects have been started")
    print(" 3. See which projects have been completed")
    print(" 4. Modify a project status")
    print(" 5. Add a new project.")
    print(" Q: Quit")
    user_action = input("")

    print("USER ACTION: ", user_action)

    if user_action == '1':
        result = get_list_of_projects()
        print(result)
    elif user_action == 'q' or user_action == 'Q':
        print("Quitting App")
        return False
    else:
        print("Option Not Available - Stay Tuned ... ")

    return True


run_program = True
while run_program:
    run_program = user_menu()