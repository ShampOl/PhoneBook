import os

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, data, variant):
        folder_name = f"data_{variant}_variant"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = os.path.join(folder_name, f"{name}.txt")

        with open(file_path, 'w') as file:
            file.write(data)

        self.contacts[name] = file_path

    def display_contacts(self, format_option):
        print("Телефонный справочник:")
        for name, file_path in self.contacts.items():
            with open(file_path, 'r') as file:
                data = file.read()

                if format_option == 1:
                    print(f"{name}:\n{data}")
                elif format_option == 2:
                    print(f"{name}: {'; '.join(data.splitlines())}")

    def update_contact(self, name, new_data, variant):
        folder_name = f"data_{variant}_variant"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = os.path.join(folder_name, f"{name}.txt")

        with open(file_path, 'w') as file:
            file.write(new_data)

        self.contacts[name] = file_path
        print(f"Контакт {name} обновлен.")

    def delete_contact(self, name):
        if name in self.contacts:
            file_path = self.contacts[name]
            os.remove(file_path)
            del self.contacts[name]
            print(f"Контакт {name} удален.")
        else:
            print(f"Контакт {name} не найден.")
            

def name_data():
    name = input('Введите ваше имя: ')
    return name


def contact_data():
    print("Выберите формат записи контакта:")
    print("1. Запись в столбец")
    print("2. Запись в строчку через ;")
    
    choice = input("Введите номер формата (1 или 2): ")
    
    if choice == "1":
        surname = input('Введите вашу фамилию: ')
        phone = input('Введите ваш номер телефона: ')
        address = input('Введите ваш адрес: ')
        return f"Фамилия: {surname}\nТелефон: {phone}\nАдрес: {address}"
    elif choice == "2":
        surname = input('Введите вашу фамилию: ')
        phone = input('Введите ваш номер телефона: ')
        address = input('Введите ваш адрес: ')
        return [f"Фамилия: {surname}", f"Телефон: {phone}", f"Адрес: {address}"]
    else:
        print("Неверный ввод. Используется формат 1.")
        surname = input('Введите вашу фамилию: ')
        phone = input('Введите ваш номер телефона: ')
        address = input('Введите ваш адрес: ')
        return f"Фамилия: {surname}\nТелефон: {phone}\nАдрес: {address}"


if __name__ == "__main__":
    phone_book = PhoneBook()

    while True:
        print("\n1. Добавить контакт")
        print("2. Показать контакты")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            name = name_data()
            data = contact_data()
            variant = input("Выберите вариант записи (1 или 2): ")
            phone_book.add_contact(name, data, variant)
        elif choice == "2":
            print("\nВыберите формат отображения контактов:")
            print("1. Запись в столбец")
            print("2. Запись в строчку через ;")
            format_option = input("Введите номер формата (1 или 2): ")
            phone_book.display_contacts(int(format_option))
        elif choice == "3":
            name = input("Введите имя контакта для изменения: ")
            new_data = contact_data()
            variant = input("Выберите вариант записи (1 или 2): ")
            phone_book.update_contact(name, new_data, variant)
        elif choice == "4":
            name = input("Введите имя контакта для удаления: ")
            phone_book.delete_contact(name)
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")
