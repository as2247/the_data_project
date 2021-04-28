"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module tui
        any processing should be done using the appropriate functions in the module process
        any database related querying should be done using the appropriate functions the module database
        any visualisation should be done using the appropriate functions in the module visual
"""

# Task 19: Import required modules
# TODO: Your code here

# Task 20: Create an empty list named 'records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here


def run():

    # Task 21: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here

    while True:
        # Task 22: Use the appropriate function in the module tui to display the main menu
        # and retrieve the user's desired selection.
        # This should be assigned to a suitable local variable
        # You should remove the keyword pass below before you start this task
        # TODO: Your code here
        pass

        # Task 23: Check if the user selected the option for loading data.
        # If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # data loading operation has started.
        # - Load the data by doing the following:
        #   - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.
        #   - Read each line from the CSV file (as a list of values) and add it to the list 'records'.
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # data loading operation has completed.
        # TODO: Your code here

        # Task 29: Check if the user selected the option for processing data.
        # If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # data processing operation has started.
        # - Process the data by doing the following:
        #   - call the appropriate function in the module tui to determine what processing is to be done.
        #   - call the appropriate function in the module process and display the results
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # data processing operation has completed.

        # Task 36: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module tui to determine what querying is to be done.
        #   - call the appropriate function in the module database and display the results
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # database querying operation has completed.

        # Task 40: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module tui to determine what visualisation is to be done.
        #   - call the appropriate function in the module visual
        # - Use the appropriate function in the module tui to display a message to indicate that the
        # data visualisation operation has completed.

        # Task 41: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 42: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here


if __name__ == "__main__":
    run()
