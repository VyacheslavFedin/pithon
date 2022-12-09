
def menu_number_3():
    a = input('введите фамилию : ')
    b = input('введите имя : ')
    c = input('введите отчество : ')
    d = input('введите номер телефона : ')

    data = open('data.txt', 'a')
    data.write('\n' + a + '\n' + b + '\n' + c + '\n' + d)
    data.close()