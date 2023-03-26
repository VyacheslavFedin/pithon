import json
from pprint import pprint
import os

def menu_number_1():

    isempty = os.stat('data_file.json').st_size == 0
    if isempty==True :
        print ('заметок нет')
    else:
        with open("data_file.json", "r") as read_file:
            file = json.load(read_file)
        pprint(file)
