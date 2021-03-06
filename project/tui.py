import csv

"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

"""
The following functions are related to requirements a) and b) of the assessment
"""


def welcome():
    print(" ---------------- \nMovies Data System \n ----------------")


def main_menu():
    print(""" Please select an option:
    [1] Load Movies
    [2] Process Movies
    [3] Query Movies
    [4] Visualise Movies
    [5] Exit
    """)
    selected_option = int(input())
    if 0 < selected_option < 6:
        print(f"You have selected option {selected_option}")  # Test return value is an integer
        return selected_option
    else:
        print("ERROR: Please select a valid option ")


def data_file_path():
    file_path = input("Please enter a file path")
    suffix = '.csv"'

    if file_path.endswith(suffix):
        print(f"File Path: {file_path}")
        return file_path
    else:
        print("Error! Please enter a valid csv file path (.csv)")



"""
The following functions are related to requirement c) of the assessment i.e. processing
"""


def started(operation):
    """
    Task 4: Display a message to indicate that an operation has started.

    The function should display a message in the following format:

    "{operation} has started."

    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here


def completed(operation):
    """
    Task 5: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:

    "{operation} has completed."

    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here


def error(error_msg):
    """
    Task 6: Display an error message.

    The function should display a message in the following format:

    "Error! {error_msg}."

    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here


def process_menu():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:

    [1] Retrieve the total number of movies
    [2] Retrieve an individual movie
    [3] Retrieve specific data for an individual movie
    [4] Retrieve all movies for a specified release year
    [5] Retrieve all movies in the specified genres

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve the total number of movies', 2 for 'Retrieve an individual movie' and so on.

    :return: an integer corresponding to a valid selection
    """
    # TODO: Your code here


def total_movies(num_movies):
    f"""
    Task 8: Display the total number of movies in the data set.

    The function should display a message in the following format:

    "There are {num_movies} in the data set."

    Where {num_movies} is the value of the parameter passed to this function

    :param num_movies: the total number of movies in the data set
    :return: Does not return anything
    """
    # TODO: Your code here


def movie_name():
    """
    Task 9: Read in the name of a movie and return the name.

    The function should ask the user to enter the name of a movie e.g. "Avengers: End Game"
    The function should then read in and return the user's response.

    :return: the name of a movie
    """
    # TODO: Your code here


def movie_year():
    """
    Task 10: Read in and return the release year for a movie.

    The function should ask the user to enter the year in which a movie is released e.g. "2021"
    The function should then read in and return the user's response as an integer.

    :return: the release year of a movie as an integer
    """
    # TODO: Your code here


def movie_genres():
    """
    Task 11: Read in and return the genres for a movie.

    The function should ask the user to enter one or more movie genres.
    These should be entered as comma separated values e.g. "Comedies, Dramas"
    The function should read in the user's response and return a list of genres e.g. ["Comedies", "Dramas"].

    :return: a list of genres
    """
    # TODO: Your code here


def movie_actors():
    """
    Task 12: Read in and return the actors for a movie.

    The function should ask the user to enter one or more movie actors.
    These should be entered as comma separated values e.g. "Scott Hussion, Seth Fuller"
    The function should read in the user's response and return a list of actors
    e.g. ["Scott Hussion", "Seth Fuller"].

    :return: a list of actors
    """
    # TODO: Your code here


def movie_details():
    """
    Task 13: Read in the name of a movie and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of a movie e.g. "Batman"
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the movie and the list of column
    indexes e.g. ["Batman", [0,1,5,7]]

    :return: A list containing the name of a movie and a list of column indexes
    """
    # TODO: Your code here


def display_movie(movie, cols=None):
    """
    Task 14: Display a movie. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the movie will be displayed.

    The parameter movie is a list of values e.g. [18,"13 Sins",93,2014,"Horror Movies, Thrillers",...]
    The parameter cols is a list of column indexes e.g. [0,1,5,7]
    The function should a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the entity [18,"13 Sins",93,2014,"Horror Movies, Thrillers",...]
    the following should be displayed:
    ["13 Sins",2014]

    E.g. if cols is [0,1,4] then for the entity [18,"13 Sins",93,2014,"Horror Movies, Thrillers",...]
    the following should be displayed:
    [18,"13 Sins","Horror Movies, Thrillers"]

    E.g. if cols is an empty list or None then all the values will be displayed
    [18,"13 Sins",93,2014,"Horror Movies, Thrillers",...]

    :param movie: A list of data values for a movie
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here


def display_movies():
    """
    Task 15: Display each movie in movies. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a movie will be displayed.

    The function should have two parameters as follows:

    movies      which is a list of movies where each movie itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each movie in movies and display the movie.

    Each movie should be displayed as a list of values e.g. [216,"Ali",157,2001,"Dramas, Sports Movies",...]
    Only the columns whose indexes are included in cols should be displayed for each movie.

    If cols is an empty list or None then all values for the entity should be displayed.

    :param movies: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here


"""
The following functions are related to requirements d) and e) of the assessment i.e. database
"""


def database_menu():
    """
    Task 16: Display a menu of options for how database should be queried. Read in the user's response.

    A menu should be displayed that contains the following options:

    [1] Setup database
    [2] Retrieve all directors from database
    [3] Retrieve top 5 movies from database
    [4] Retrieve top 5 movies per country from database
    [5] Retrieve top 5 movies per country for specific genre from database
    [6] Retrieve movies starring specific actor from database

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for "Setup database", 2 for "Retrieve all directors from database" and so on.

    :return: an integer corresponding to a valid selection
    """
    # TODO: Your code here


def display_query_results():
    """
    Task 17: Display the results of querying the database

    This function should take a single parameter as follows:

    rows        the rows retrieved from the database after querying the database

    You will need to add this parameter to the function definition.

    The function should iterate through each row in rows and suitably display the row.

    :param rows: the rows from the database
    :return: Does not return anything
    """


"""
The following functions are related to requirements f) of the assessment i.e. visualisation
"""


def visual_menu():
    """
    Task 18: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:

    [1] Display the number of movies in each genre
    [2] Display the number of movies per country
    [3] Display top movies per country and for specific genre

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for "Display the number of movies in each genre" and so on.

    :return: an integer corresponding to a valid selection
    """
    # TODO: Your code here


def run():
    # welcome()
    # main_menu()
    data_file_path()


if __name__ == "__main__":
    run()