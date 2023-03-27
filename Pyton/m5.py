import json
from pprint import pprint
import os

def menu_number_5():
    my_dict = {}

    isempty = os.stat('data_file.json').st_size == 0
    if isempty == True:
        print('заметок нет')
    else:
        with open("data_file.json", "r") as read_file:
            my_dict = json.load(read_file)

    day = str(input('введите необходимую дату в формате ДД-ММ-ГГГГ :'))


    for key, value in my_dict.items():
        time = ''
        for i in range(0, 10):
            time = str(time + key[i])
        if day == time:
            print(key, value)
