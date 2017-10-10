"""
 This is the helper file. 
 It contains a list of functions that would be re-used 
 This file is imported in the program.py file

"""
from sys import exit
"""
    This function is used for validating a row on the basis of -
        a.) to validate that all the column names are found in each row’s keys
        b.) if the corresponding values are int
    :param: row -> The row to check 
    :param: headings -> The headings of the csv file 
    :return: dict -> dictionary of validate row with value as key
    format -> {key: int_value, key1L int_value......}
"""

def validate_row_data(row, headings):
    try:
        dict = {}
        for k,v in row.items():
            if k in headings and is_positive_int(v):
                # Replace the validated values for a key into to the dictionary.
                dict[k] = int(v)
            else:
                return False
        return dict
    except Exception as e:
        print(e.__class__.__name__)


"""
    Check if the parameter provided is an integer
    :param: value -> The value to check
    :return: True if an integer else Flase
"""
def is_positive_int(value):
    try:
        int(value)
        if int(value) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

"""
    This function validates the user input on the following condition:-
        0 < value < 8
    :param: user_in -> The input entered by the user
    :reutrn: True/False based on the condition
"""
def validate_user_input(user_in):
    if is_positive_int(user_in) and int(user_in) < 8:
        return True
    else:
        return False

"""
    This func checks if the floor value entered by user is correct
    :param: user_in -> The input by the user 
    :return: True/False based on the validating conditions
"""
def validate_floor_value(user_in):
    if is_positive_int(user_in):
        return True
    else:
        return False

"""
    This function helps gettings user inputs 
    :param: **kwargs 
        1.) question -> The question to ask user 
        2.) validate_func -> The func to call to validate user input 
        3.) question2 -> Question to ask user if enters wrong info
        4.) counter -> to check how many times user has entered data 
"""
def get_user_data(**kwargs):
    try:
    
        # this cleans the dictionary for the features that this func provides
        options = ['question', 'validate_func', 'alert', 'counter']
        for k,v in kwargs.keys():
            print(k, v)
            if k not in options:
                kwargs.pop(k, v)
        
        user_in = input(kwargs[question])

        if kwargs[validate_func](user_in):
            return int(user_in)
        else:
            kwargs[counter] += 1
            check_counter(kwargs[counter])
            print(kwargs[alert])
            get_user_input(kwargs)

    except AttributeError as e:
        print("The function you are trying to call doesnot exist")

"""
    This function checks if the user entered an input incorrectly thrice
    Exits the program if the user exceeds the number of try's
    :param: counter -> The number of tries by the user
    
"""
def check_counter(counter):
    if counter == 3:
            print("You entered input incorrectly thrice. Exiting the program")
            exit(2)
