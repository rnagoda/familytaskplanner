import mysql.connector
from mysql.connector import Error
from resources import config_vals


def run_query_return_list(query) -> list:
    """
    Connects to the db, runs the query and disconnects
    :param query: String representing MySQL query
    :return: result of query
    """

    try:
        connection = mysql.connector.connect(host=config_vals.db_host,
                                             database=config_vals.db_name,
                                             user=config_vals.db_user,
                                             password=config_vals.db_password)

        if connection.is_connected():
            db_info = connection.get_server_info()
            # print("Connected to MySQl Server Version: ", db_info)
            cursor = connection.cursor()
            record = cursor.fetchone()
            # print("You're connected to the db: ", record)
            # print("Running query: ", query)
            cursor.execute(query)
            result = cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)

    else:
        cursor.close()
        connection.close()
        # print('MySQL connection is closed.')

    return result


def get_list_of_projects() -> list:
    """
    Return a list of projects from the DB

    :return: Project list
    """
    query = 'SELECT * FROM projects'
    project_list = run_query_return_list(query)
    return project_list


def get_list_of_projects_status_started() -> list:
    """
    Return a list of projects with status 'Started'

    :return: Project list
    """
    query = f"SELECT * " \
            "FROM projects " \
            "WHERE status = " \
            "(SELECT id " \
            "FROM " + config_vals.status_table + " "\
            "WHERE name = 'started');"

    project_list = run_query_return_list(query)

    return project_list


def get_list_of_statuses() -> list:
    """
    Return a list of project statuses

    :return: Status list
    """

    query = f"SELECT * FROM {config_vals.status_table}"

    return run_query_return_list(query)
