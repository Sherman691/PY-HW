from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ Каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def remove(ref_numb):    
    if ref_numb == 1:
        with open('data_first_variant.csv', 'r') as file:
            name_del = input("Введите имя, которое хотите удалить: ")+"\n"
            lines = file.readlines()
            name_del_index = lines.index(name_del)

        del lines[name_del_index: name_del_index + 5]

        with open('data_first_variant.csv', 'w') as file: 
            for line in lines:
                file.write(line)
        print_data()


    if ref_numb == 2:
        with open('data_second_variant.csv', 'r') as file:
            name_del = input("Введите имя, которое хотите удалить: ")
            lines = file.readlines()
            

        with open('data_second_variant.csv', 'w') as file:
            for line in lines:
                if name_del not in line:
                    file.write(line)
        print_data()                


def print_data():
    print('1 справочник:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 справочник:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

      
    command = int(input("1 - Ввести новые данные \n"
                        "2 - Удалить данные \n"
                        "3 - Выход \n"))
    
    
    while command < 1 or command > 3:
        print("Ошибка ввода!\n")
        command = int(input("1 - Ввести новые данные \n"
                            "2 - Удалить данные \n"
                            "3 - Выход \n"))        
    if command == 1:        
        input_data()
    elif command ==2:
        remove(int(input("Введите номер справочника: ")))
    elif command == 3:
        return
    

