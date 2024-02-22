from data_create import name_data, surname_data, phone_data, address_data

DATA_FILE_FIRST = 'data_first_variant.csv'
DATA_FILE_SECOND = 'data_second_variant.csv'
DELIMITER = ';'

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(
        f'В каком формате Вы хотите сохранить?\n\n1 вариант:\n{name}\n{surname}\n{phone}\n{address}\n'
        f'2 вариант : \n{name}{DELIMITER}{surname}{DELIMITER}{phone}{DELIMITER}{address}\n Введите Ваш вариант: '))

    while var not in (1, 2):
        print('Ошибка. Повторите попытку.')
        var = int(input('Введите вариант: '))

    if var == 1:
        data_line = f'{name}\n{surname}\n{phone}\n{address}\n\n'
    else:
        data_line = f'{name}{DELIMITER}{surname}{DELIMITER}{phone}{DELIMITER}{address}\n\n'

    with open(DATA_FILE_FIRST if var == 1 else DATA_FILE_SECOND, 'a', encoding='utf-8') as f:
        f.write(data_line)

    return data_line

def read_data(data_file):
    print(f'Открываю телефонную книгу в {"" if data_file == DATA_FILE_FIRST else "во "}втором варианте:')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(*data)
    return data

def change_data():
    data_file = choose_data_file()
    data_list = read_data(data_file)

    while True:
        name_data_d = input('Введите имя контакта, который Вы хотите изменить: ')
        
        contact_found = False
        replace_index = 0  # Индекс, с которого начнем замену данных в первом варианте

        for i in range(len(data_list)):
            if name_data_d in data_list[i]:
                new_contact_data = input_data()
                contact_found = True
                # Запоминаем индекс, чтобы начать замену данных с этого места в первом варианте
                replace_index = i
                break

        if not contact_found:
            print(f"Контакт с именем {name_data_d} не найден.")
            choice = input('Хотите повторить попытку? (1-Да, 2-Нет.): ').lower()
            if choice != '1':
                print('Выход из программы.')
                return
        else:
            # Если меняем данные в первом файле, заменяем только 4 строки
            if data_file == DATA_FILE_FIRST:
                with open(data_file, 'w', encoding='utf-8') as f:
                    # Заменяем существующие строки новыми данными
                    f.writelines(data_list[:replace_index] + [new_contact_data] + data_list[replace_index + 5:])
            # Если меняем данные во втором файле, заменяем только одну строку
            elif data_file == DATA_FILE_SECOND:
                with open(data_file, 'w', encoding='utf-8') as f:
                    # Заменяем существующую строку новыми данными
                    f.writelines(data_list[:replace_index] + [new_contact_data] + data_list[replace_index + 2:])
            break

def delete_data():
    data_file = choose_data_file()
    data_list = read_data(data_file)
    name_data_d = input('Введите имя контакта, который Вы хотите удалить: ')

    matching_contacts = [(i, contact) for i, contact in enumerate(data_list) if name_data_d in contact.split('\n')[0]]

    if not matching_contacts:
        print(f"Контакт с именем {name_data_d} не найден.")
        return

    if len(matching_contacts) > 1:
        print(f"Найдено несколько контактов с именем {name_data_d}. Выберите контакт для удаления:")
        for idx, (contact_idx, contact) in enumerate(matching_contacts, start=1):
            print(f"{idx}. {contact}")

        selected_contact = int(input())
        if selected_contact not in range(1, len(matching_contacts) + 1):
            print("Ошибка: Некорректный выбор.")
            return
        selected_contact_idx, _ = matching_contacts[selected_contact - 1]
    else:
        selected_contact_idx, _ = matching_contacts[0]

    confirmed = input(f'Вы уверены, что хотите удалить контакт "{data_list[selected_contact_idx].strip()}" (1-Да, 2-Нет): ').lower()

    if confirmed != '1':
        print('Отменено. Контакт не удален.')
        return

    with open(data_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(data_list):
            if i == selected_contact_idx:
                if data_file == DATA_FILE_FIRST:
                    i += 5
                elif data_file == DATA_FILE_SECOND:
                    i += 2
            else:
                f.write(data_list[i])
                i += 1

    print(f'Контакт "{data_list[selected_contact_idx].strip()}" успешно удален.')


def choose_data_file():
    command = int(input('В каком варианте Вы хотите работать? (1 или 2): '))
    while command not in (1, 2):
        print('Ошибка.')
        command = int(input('Повторите попытку: '))
    return DATA_FILE_FIRST if command == 1 else DATA_FILE_SECOND
