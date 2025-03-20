# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:10:03 2022
References:
    https://www.w3resource.com/python-exercises/csv/python-csv-exercise-2.php
    https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
@author: Shivani Chowdhry
"""

import csv
import os

# function to print csv files with tab delimiter
def print_csv(csv_file):
    print(csv_file + ':')
    with open(csv_file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter = ',')
        for row in data:
            print('\t'.join(row))

#function to prompt for a directory and if it 
#exists call the print csv function for all existing csv files inside
def ask_dir_print_csv():
    directory=input(" Enter the Directory\n")
    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".csv"):
                    print_csv(os.path.join(root, file))
    else:
        print('Not a Valid Directory')

#main code calling the above defined functions
ask_dir_print_csv()