# Создать телефонный справочник с возможностью импорта и экспорта данных в несколько форматов
import menu_1
import menu_2
import menu_3

print('выберите действие:')
print('1. найти номер телефона по введеной фамилии абонента')
print('2. найти ФИО абонента по введеному номеру телефона')
print('3. внести нового абонента')
  
menu_number = int(input('введите номер пункта меню: '))

if menu_number == 1:
    menu_1.menu_number_1()

if menu_number == 2:
    menu_2.menu_number_2()

if menu_number == 3:
    menu_3.menu_number_3()
