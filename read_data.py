def read_data_to_text():
    data = open('data.txt')
    text_file = data.readlines()
    #global text
    text = []
    for i in text_file:
        text.append(i) 
    data.close()
    return text