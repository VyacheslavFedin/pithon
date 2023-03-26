import json
from pprint import pprint

def menu_number_3():
    key = str(input('скопируйте дату заметки : '))
    my_dict = {}

    with open("data_file.json", "r") as read_file:
        my_dict = json.load(read_file)

    del my_dict[key]

    with open("data_file.json", "w") as w_f:
        json.dump(my_dict, w_f)
