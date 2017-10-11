"""
 This is the helper file. 
 It contains a list of functions that would be re-used 
 This file is imported in the program.py file

"""

# imports 
from sys import exit
import os



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
        print(str(e))
        print("A problem occured while validating the row data ")
        exit(2)


"""
    Check if the parameter provided is an integer and is > -1
    :param: value -> The value to check
    :return: True if an integer else Flase
"""
def is_positive_int(value):
    try:
        int(value)
        if int(value) >= 0:
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
    if is_positive_int(user_in) and 0 < int(user_in) < 8:
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
        for k in kwargs.keys():
            if k not in options:
                kwargs.pop(k, v)
        
        user_in = input(kwargs["question"])
        check_quit(user_in)

        if kwargs["validate_func"](user_in):
            return int(user_in)
        else:
            kwargs["counter"] += 1
            check_counter(kwargs["counter"])
            print(kwargs["alert"])
            # we return this so that we donot run into the problem of stack 
            return get_user_data(**kwargs)

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

"""
    This function updates the name of the colum from an int to its respective value 
    :param: headings -> THe headings in the file 
    :param: colum_name -> THe int value of the colum
"""
def get_colum_name(headings, colum_name):
    if len(headings):
        headings = enumerate(headings)
        for k, v in headings:
            if k == colum_name:
                colum_name = v
        return colum_name
    else:
        return False


"""
    This function prompts the user for file name 
    Check if the filname has .csv in end if not then adds it 
    Checks if the file already exists and if it does reprompt the user
    :param: path -> Path where the file would be saved
    :param: ques -> The question that will be prompted to the user 
    :return: fname -> The name of the file after doing checks
"""
def get_file_name_and_make_path(path,
                                ques="Please enter the name of the file to save data to: ", counter=0):
    try:
        orignal_path = path
        fname = input(ques)
        check_quit(fname)

        if fname[-4:] != ".csv":
            # check if the file has .csv in end if not then add it 
            fname = fname + ".csv"

        path = os.path.join(path, fname) 

        # check if file already exits if yes prompt user again not more than 3 times
        if os.path.isfile(path):
            counter += 1
            check_counter(counter)
            # we return this otherwise we were running into a problem
            # where the value of the previous function call in the stack was getting returned
            return get_file_name_and_make_path(orignal_path, ques="The filename you entered already exists please enter a different file name: ")
        else:
            return fname

    except Exception as e:
        print(str(e))
        

"""
    THis function checks if the user input is -1 and exits 
    :param: user_in -> the input entered by users
"""
def check_quit(user_in):
    if user_in and user_in == "-1":
        exit(0)
