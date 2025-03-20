# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:52:44 2022

@author: Shivani Chowdhry
"""
# Importing file named "parcels.py"
import sys
sys.path.append('C:/Users/shiva/Desktop/Fall 2022/Python class/parcels.py')
from parcels import parcels
# Defining a function to test for errors in prompted numeric values 
def get_valid_num_prompt():
    prompt = input("Enter a valid value for Prompt : ")
    try:
        prompt = float(prompt)
    except:
        print("Invalid entry. Prompt must be numeric.")
        return get_valid_num_prompt()
    return prompt
# Prompting user for different filters
print('Your Minimum Area Filter:')
min_living_area_prompt = get_valid_num_prompt()
print('Market Value min Filter:')
market_value_min_prompt = get_valid_num_prompt()
print('Market Value max Filter:')
market_value_max_prompt = get_valid_num_prompt()
print('State Code Filter:')
state_code_prompt = str(input("Enter a valid value for Prompt above: "))
print('Elementary Name Filter:')
elementary_name_prompt = str(input("Enter a valid value for Prompt above : "))

# Setting initial count and address list and looking for criteria to match with the list of houses     
count = 0
add_list = []
for i in parcels:
    if i['living_area'] >= min_living_area_prompt and \
    i['state_code'] == state_code_prompt \
    and i['market_value'] >= market_value_min_prompt \
    and i['market_value'] <= market_value_max_prompt \
    and i['CAMPNAME'] == elementary_name_prompt:
        count += 1
        add_list.append(i['street_address'])
print('Count of houses matching the criteria:')        
print(count)
print('List of addresses matching the criteria:')
for i in add_list:
    print(i)
