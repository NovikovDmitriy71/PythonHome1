def rename_contact(phonebook,search_key): 
    search_key=search_key.capitalize()
    for i in range(len(phonebook)):
        if  search_key in phonebook[i].values():
            n=input(f"Подтвердите изменения контакта (y/n):  ")
            if n=="y":
                del phonebook[i]
                phonebook[i]['last_name'] = input("Фамилия: ")
                phonebook[i]['first_name'] = input("Имя: ")
                phonebook[i]['middle_name'] = input("отчество:  ")  
                phonebook[i]['phone_namber'] = input("телефон:  ") + "\n"
                print(phonebook)
                n=="y"
            else:
                break

def remove_contact(phonebook, search_key):
    search_key=search_key.capitalize()
    for i in range(len(phonebook)):
        if search_key in phonebook[i].values():
            n=input(f"Падтвердите изменения контакта (y/n):  ")
            if n=="y":
                del phonebook[i]
            return (search_key)

def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name, 
                    'phone_number': phone_number
                })
            print('Данные успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    return phonebook


def search_contact(phonebook, search_key):
    results = []
    for contact in phonebook:
        if (search_key in contact['last_name'] or search_key in contact['first_name']):
            results.append(contact) 
    return(results)       

def views_contacts(phonebook):
    for index, contact in enumerate(phonebook,start=1):
        print(f"{index}.  {contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']} \n")

def save_to_file(filename,phonebook):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f" {contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']} \n")
        print('Данные сохранены')

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact={
    'last_name': last_name,
    'first_name': first_name,
    'middle_name': middle_name,
    'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Данные добавлены')

def main():
    phonebook=[]

    filename='contacts.txt'
    while True:
        print ("1. Добавить контакт ")
        print ("2. Сохранить файл ") 
        print ("3. Вывести все контакты ")
        print ("4. Поиск по Имени/Фамилии ")
        print ("5. Загрузить из файла ")
        print ("6. Удалить контакт ")
        print ("7. Редактировать контакт ")
        print ("8. Выйти ")


        choice =input("Выберите действие ")
        if choice == '1':                      # Добавление контакта
            last_name    = input('Фамилия: ')
            first_name   = input('Имя: ')
            middle_name  = input('Отчество: ')
            phone_number = input('телефон: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':                    # Сохранение контактов в файле
            save_to_file(filename, phonebook)
        elif choice == '3':                     # Просмотр списка контактов
            views_contacts(phonebook)
        elif choice == '4':                     # Поиск контакта
            search_key = input("Введите Имя или Фамилию для поиска: ")
            search_contact(phonebook, search_key)
            results = search_contact(phonebook,search_key)
            if (results):
                print('Найдены контакты')
                print(results)
            else:
                print('контактов по запросу нет')
        elif choice == '5':                     # Загрузка контактов из файла
            phonebook=load_file(filename)
        elif choice == '6':                     # Удаление контакта
            search_key = input("Введите Имя или Фамилию для поиска: ")
            remove_contact(phonebook, search_key)
            if (search_key):
                print('Найденый контакт удален')
            else:
                print('Контактов по запросу не найдено')
        elif choice == '7':
            search_key = input("Введите Имя или Фамилию для поиска: ")
            rename_contact(phonebook,search_key)
            if n=="y":
                print("Контакт изменен")
            else:
                print("Контакт без изменений")
        elif choice == '8':
            break
        else:
            print('Не корректный выбор')
    
if __name__== "__main__":
    main() 
