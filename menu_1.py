import read_data 
text = read_data.read_data_to_text()

def menu_number_1():
    
    fio = input('введите фамилию абонента с большой буквы : ')
    for i in range (len(text)):
        if fio+'\n' == text[i]:
            print(text[i],text[i+1],text[i+2],'tel.:',text[i+3])  

    