from datetime import datetime
import json
from pprint import pprint
import os
import uuid


def menu_number_2():
    title = input('введите заголовок: ')
    msg = input('введите текст заметки : ')
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    user_id = str(uuid.uuid1())

    val = [title, msg, user_id]
    my_dict = {}

    # my_path = os.path.exists('data_file.json')
    # if my_path == True:
    isempty = os.stat('data_file.json').st_size == 0
    if isempty == True:
        my_dict[time] = val
    else:
        with open("data_file.json", "r") as read_file:
            my_dict = json.load(read_file)

    my_dict[time] = val

    with open("data_file.json", "w") as w_f:
        json.dump(my_dict, w_f)
