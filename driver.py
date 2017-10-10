"""
 This file is the main driver of the program. 
 This file imports logic.py. 
 THe reason for doing this is to keep the code organized and prevent clustering in one file

"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import logic
import sys

def main():
    # this program gives user an option to enter the path of the file at command prompt
    if len(sys.argv) == 2:
        data = logic.load_cencus_data(sys.argv[1])
    else:
        data = logic.load_cencus_data()

    # ask the user for which coloum to filter data by
    colum_value = logic.get_user_input(1)
    floor_value = logic.get_user_input(2)


if __name__ == "__main__":
    main()
