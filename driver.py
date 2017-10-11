"""
 This file is the main driver of the program. 
 This file imports logic.py. 
 THe reason for doing this is to keep the code organized and prevent clustering in one file

"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import logic
import sys
from helper import check_quit

DEBUG = False

def main():
    print("Welcome to the program. Enter -1 at any time to exit the program")

    # this is to print out some variables if we are working in Debug env
    global DEBUG

    # this program gives user an option to enter the path of the file at command prompt
    if len(sys.argv) == 2:
        data = logic.load_cencus_data(sys.argv[1])
    else:
        data = logic.load_cencus_data()

    # ask the user for which coloum to filter data by
    if DEBUG:
        # work with sample values
        colum_value = 5
        floor_value = 1000
    else:
        colum_value = logic.get_user_input(1)
        floor_value = logic.get_user_input(2)

    # filter the data
    filtered_tuple = logic.filter_data_by_colum_and_floor(data, colum_value, floor_value)

    # check if there exists some data otherwise prompt the user that this happened
    if filtered_tuple == False:
        # this makes sure that the data recived is not empty i.e no mathches
        print("There are no values that are greater than or equal to the floor value: {} in colum ".format(floor_value))
        user_in = input("Restarting the program: Enter -1 to quit or anything else to continue ")
        check_quit(user_in)
        main()

    else:
        # get the tuple with the only column required
        filtered_tuple = logic.get_data_by_colum(filtered_tuple, colum_value)

        # sort the filtered data
        filtered_tuple = logic.sord_filtered_data(filtered_tuple, colum_value)

        # write to the csv file
        logic.write_to_csv(filtered_tuple)
        
        print("The program has ended and your csv file is stored in the exports directory")

        user_in = input("Enter -1 to quit the program press any other key to start again: ")
        check_quit(user_in)





if __name__ == "__main__":
    main()
