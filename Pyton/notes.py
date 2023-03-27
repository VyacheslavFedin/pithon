from pprint import pprint
import m1
import m2
import m3
import m4
import m5

menu_number = 0

while menu_number != 6:
    print('выберите действие:')
    print('1. распечатать на экран все заметки ')
    print('2. добавить заметку')
    print('3. удалить заметку')
    print('4. редактировать заметку')
    print('5. выбрать заметки за определенный день')
    print('6. выйти')

    menu_number = int(input('введите номер пункта меню: '))

    if menu_number == 1:
        m1.menu_number_1()

    if menu_number == 2:
        m2.menu_number_2()

    if menu_number == 3:
        m3.menu_number_3()

    if menu_number == 4:
        m4.menu_number_4()

    if menu_number == 5:
        m5.menu_number_5()
