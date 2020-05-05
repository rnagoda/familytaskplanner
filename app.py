import userActions as user_actions


def main():
    run_program = True
    while run_program:
        run_program = user_actions.present_user_menu()


if __name__ == "__main__":
    main()
