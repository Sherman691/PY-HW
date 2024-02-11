from logger import input_data, print_data


def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что выхотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Выход')
          
    command = int(input('Ваш выбор: '))

    while command <1 or command > 3:
        command = int(input('Ошибка. Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command ==3:
        return

interface()