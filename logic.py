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

# declared this as a global variable
# in capital becuase value remains constant to differentiate
DEBUG = False

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
    :param: input_for -> This is used to differentiate what the function is being called for 
        1 -> user input for colum based on ennumeration
        2 -> user input for floor value 
    :return: The integer value of the user input
"""
def get_user_input(input_for):
    try:
        global DEBUG
        if input_for == 1:
            global headings
            temp = enumerate(headings)
            for enum in temp:
                print("{}) {}".format((enum[0] + 1), enum[1]))
            
            #helper function takes care of the checking
            value = helper.get_user_data(question="Please enter an integer based on one of the ennumeration EG 1 for Zip Code: ",
                                 validate_func = helper.validate_user_input,
                                 alert = "Please enter a valid number betweeen 1 and 7",
                                 counter = 0)
            # Just a design desion we dont ask the user to enter value from 0 
            # but start from 1 and we adjust it here
            value = value - 1

        elif input_for == 2:
            value = helper.get_user_data(question="Please enter a floor value: ",
                                 validate_func = helper.validate_floor_value, 
                                 alert="Please enter a valid floor value",
                                 counter = 0)
        return value

    except Exception as e:
        print(str(e))
        print("An error occured please re-enter a valid value")
        sys.exit(1)


"""
    This function creates a new list from the data based on the colum and the floor_value
    NOTE - This function removes the reduandant step of first returning the rows 
           and then then filtering through the rows for the colum. 
    This function straight away returns the colum and value tuple
    filtered based on the users input
    :param: data -> Validated tuple of data from csv file 
    :param: colum_name -> The colum to filter data by 
    :param: floor_value -> The value to check if value greater than or equal to 
    :return: tuple of the new list created
"""
def filter_data_by_colum_and_floor(data, colum_name, floor_value):
    try: 
        # get the name of the heading based on the int value
        global headings 
        if len(headings) == 0:
            load_cencus_data()

        colum_name = helper.get_colum_name(headings, colum_name)

        #loop through the validated data
        filtered_data = []
        for row in data:
            for k,v in row.items():
                if k == colum_name and row[colum_name] >= floor_value:
                    filtered_data.append(row)

        if len(filtered_data):
            return tuple(filtered_data)    
        else: 
            return False 
    except Exception as e:
        print("A proble occured while running the program")
        print(str(e))

"""
    This function gets the only colum required based on the colum entered by the user
    :param: data -> The filtered data which has all the values in the dict
    :param: colum_name -> The int value of the column to get 
    :return: dictionary with the colum required
"""
def get_data_by_colum(data, colum_name):

    try: 
        # get the name of the heading based on the int value
        global headings
        if len(headings) == 0:
            load_cencus_data()

        colum_name = helper.get_colum_name(headings, colum_name)

        filtered_list = []
        for row in data:
            for k, v in row.items():
                if k == colum_name:
                    filtered_list.append({k: v})

        if len(filtered_list):
            return tuple(filtered_list)
        else:
            return False

    except Exception as e:
        print("Problem in the get_data_by_colum function")
        print(str(e))
        


"""
    This function sorts the filtered data 
    :param: data -> The data to sort
    :param: colum_name -> the colum to solve by (int value)
    :return: sorted data
"""
def sord_filtered_data(data, colum_name):
    try:
        global headings
        if len(data):
            # just make sure that the data recieved is not empty
            colum_name = helper.get_colum_name(headings, colum_name)
            return sorted(data, key=lambda x: x[colum_name]) 

    except Exception as e:
        print(str(e))


"""
    This is the function that deals with writing filtered, sorted data to a file
    Saves the file in a folder called exports
    Uses helper method get_file_name_and_make_path
    :param: data -> The filtered and the sorted tuple of the dictionaries with a particular column.
"""
def write_to_csv(data):
    try:
        # we create a constant DIR capital letters just to differentiate that its value would not change
        DIR = 'exports'
        if os.path.isdir(DIR) is False:
           os.mkdir(DIR)
        path = os.path.join(os.getcwd(), DIR)

        # get the file name and check if it doesnot already exists
        fname = helper.get_file_name_and_make_path(path)
        path = os.path.join(path, fname)

        # get fieldname so that we donot have to hardcode it 
        for key in data[0].keys():
            fields = [key]

        # open a file and WRITE to it 
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fields)            
            writer.writeheader()

            for row in data:
                writer.writerow(row)
        
        #returns true after the program has finished
        return True



    except Exception as e:
        print(str(e))
