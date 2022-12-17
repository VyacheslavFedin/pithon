# Создайте программу для игры в ""Крестики-нолики"".

mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_mas():
    print()
    for i in range(len(mas)):
        for i2 in range(len(mas[i])):
            print(mas[i][i2], end=' ')
        print()


print_mas()
q = 0
while q == 0:

    player = int(input('игрок 1, введите номер поля :'))

    for i in range(len(mas)):
        for i2 in range(len(mas[i])):
            if mas[i][i2] == player:
                mas[i][i2] = 'X'
    print_mas()

    if mas[0][0] == 'X' and mas[0][1] == 'X' and mas[0][2] == 'X':
        print('игрок 1 победил')
        break
    elif mas[1][0] == 'X' and mas[1][1] == 'X' and mas[1][2] == 'X':
        print('игрок 1 победил')
        break
    elif mas[2][0] == 'X' and mas[2][1] == 'X' and mas[2][2] == 'X':
        print('игрок 1 победил')
        break
    elif mas[0][0] == 'X' and mas[1][1] == 'X' and mas[2][2] == 'X':
        print('игрок 1 победил')
        break
    elif mas[2][0] == 'X' and mas[1][1] == 'X' and mas[0][2] == 'X':
        print('игрок 1 победил')
        break
    elif mas[0][0] == 'X' and mas[1][0] == 'X' and mas[2][0] == 'X':
        print('игрок 1 победил')
        break
    elif mas[0][1] == 'X' and mas[1][1] == 'X' and mas[2][1] == 'X':
        print('игрок 1 победил')
        break
    elif mas[0][2] == 'X' and mas[1][2] == 'X' and mas[2][2] == 'X':
        print('игрок 1 победил')
        break

    player = int(input('игрок 2, введите номер поля : '))

    for i in range(len(mas)):
        for i2 in range(len(mas[i])):
            if mas[i][i2] == player:
                mas[i][i2] = 'O'
    print_mas()

    if mas[0][0] == 'O' and mas[0][1] == 'O' and mas[0][2] == 'O':
        print('игрок 2 победил')
        break
    elif mas[1][0] == 'O' and mas[1][1] == 'O' and mas[1][2] == 'O':
        print('игрок 2 победил')
        break
    elif mas[2][0] == 'O' and mas[2][1] == 'O' and mas[2][2] == 'O':
        print('игрок 2 победил')
        break
    elif mas[0][0] == 'O' and mas[1][1] == 'O' and mas[2][2] == 'O':
        print('игрок 2 победил')
        break
    elif mas[2][0] == 'O' and mas[1][1] == 'O' and mas[0][2] == 'O':
        print('игрок 2 победил')
        break
    elif mas[0][0] == 'O' and mas[1][0] == 'O' and mas[2][0] == 'O':
        print('игрок 2 победил')
        break
    elif mas[0][1] == 'O' and mas[1][1] == 'O' and mas[2][1] == 'O':
        print('игрок 2 победил')
        break
    elif mas[0][2] == 'O' and mas[1][2] == 'O' and mas[2][2] == 'O':
        print('игрок 2 победил')
        break
