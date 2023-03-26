import json
from pprint import pprint
import uuid


def menu_number_4():
    key = str(input('скопируйте дату заметки : '))
    title = input('введите заголовок: ')
    msg = input('введите текст заметки : ')
    user_id = str(uuid.uuid1())
    val = [title, msg, user_id]
    my_dict = {}
    
    with open("data_file.json", "r") as read_file:
        my_dict = json.load(read_file)
    
    
    my_dict[key] = val

    with open("data_file.json", "w") as w_f:
        json.dump(my_dict, w_f)
