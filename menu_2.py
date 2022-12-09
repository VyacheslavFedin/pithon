import read_data 
text = read_data.read_data_to_text()

def menu_number_2():
    
    tel = input('введите номер телефона : ')
    for i in range(len(text)):
        if tel == text[i] or tel+'\n' == text[i]:
            print(text[i-3],text[i-2],text[i-1],'tel.:',text[i])
    