from logger import input_data, read_data, change_data, delete_data


def interface():
    while True:
        print('Добро пожаловать в бот-справочник. Выберите команду:\n1: Добавить контакт\n2: Открыть список контактов\n3: Изменить контакт\n4: Удалить контакт\n5: Выход')
        try:
            command = int(input('Выберите команду (1-5): '))
        except ValueError:
            print('Ошибка: введите число от 1 до 5.')
            continue

        if command == 1:
            input_data()
        elif command == 2:
            read_data()
        elif command == 3:
            change_data()
        elif command == 4:
            delete_data()
        elif command == 5:
            print('Выход из программы.')
            break
        else:
            print('Ошибка: введите число от 1 до 5.')

        another_command = input('Хотите выполнить еще одну команду? (y/n): ').lower()
        if another_command != 'y':
            break

