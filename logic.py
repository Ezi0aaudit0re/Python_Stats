"""
    This file contains the logic of the program 
    This file has the main functions 
    1.) load_cencus_data
    2.) filter_data_by_colom and floor

    This file also imports few modules namely 
    1.) os 
    2.) sys
    3.) helper - self designed to help with the program 
    4.) csv - to read csv file
"""

""""""""""" Imports """""""""
import os 
import sys
import helper
import csv

# this variable would store headings (the coloms of the csv file)
headings = ()

DEBUG = True

"""
    This function loads the data from the csv file into the memory
    It validates the rows and then loads them on the memory
    :param: path -> The path to the csv file 
    :return: a tuple of valid data
"""
def load_cencus_data(path="./file.csv"):
    try:
        if(os.path.isfile(path) == False):
            # this checks if the path provided to the file exists
            print("Please provide with a correct file path. You can provide the file path as an argument when running the program EG python driver.py <path to file> ")
            sys.exit(1)

        global headings
        global DEBUG # this checks if DEBUG mode is turned on
        validated_rows = [] # list of validated rows
        if DEBUG:
            not_validated_rows = []

        # open the file to read 
        with open(path, "r") as file:

            reader = csv.DictReader(file)

            # populate the global headings 
            # save it in the form of tupleas and not list
            headings = tuple(reader.fieldnames)

            for row in reader:
                # check if the row is valid and append the validated row to list
                result = helper.validate_row_data(row, headings)
                if result: 
                    # only add if the result is not false
                    validated_rows.append(result)
                elif DEBUG: 
                    # this is for debugging and would not run in the final version
                    not_validated_rows.append(row)

        # make sure that the file is getting closed 
        # only in Debug mode
        if DEBUG:
            assert file.closed, "The file was not closed automatically "

        return tuple(validated_rows)
            
    except AttributeError as e:
        print(str(e))
        print("An attribute Error orrucered trying again")
        
    except Exception as e:
        print("An unknown error has occured ")
        print("Please rerun the program")


"""
    This function gets an input from the user and validates it 
    If the user enters input incorrectly thrice it quits
    :param: counter -> To check the number of times user has entered an input
    :param: input_for -> This is used to differentiate what the function is being called for 
        1 -> basic user input 
        2 -> user input for floor value 
        3 -> User input for colum 
    :return: The integer value of the user input
"""
def get_user_input(input_for, counter=0):
    try:
        global DEBUG
        if input_for == 1:

            if DEBUG:
                print("In basic user input")

            global headings
            temp = enumerate(headings)
            for enum in temp:
                print("{}) {}".format(enum[0], enum[1]))

            helper.get_user_data(question="Please enter an integer based on one of the ennumeration EG 1 for Zip Code",
                                 validate_func = validate_user_input,
                                 alert = "Please enter a valid number betweeen 1 and 7",
                                 counter = 0)
            #user_in = input("Please enter an integer based on one of the ennumeration "
            #                "eg 1 for Zip Code: ")
            #if helper.validate_user_input(user_in):
            #    return int(user_in)
            #else:
            #    # updates counter and calls function recursively  
            #    counter += 1
            #    helper.check_counter(counter)
            #    print("Please enter a integer between 1 and 7")
            #    get_user_input(1, counter)

        elif input_for == 2:
        # checks if we are asking for floor value
            if DEBUG:
                print("In floor value")

            user_in = input("Please enter a postive value as floor value: ")

            if helper.validate_floor_value(user_in):
                return int(user_in)
            else: 
                # updates counter and calls the func recursively 
                counter += 1
                helper.check_counter(counter)
                print("Please enter a valid floor value")
                get_user_input(2, counter)

    except Exception as e:
        print("An error occured please re-enter a valid value")
        #get_user_input(1)


def filter_data_by_colum_and_floor(data, colum_value, floor_value):
    pass
