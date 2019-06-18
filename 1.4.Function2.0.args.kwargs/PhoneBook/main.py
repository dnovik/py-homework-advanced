from func import Contact, Phonebook
import test_data

# Создадим тестовые экземпляры контактов
sacha = Contact(*test_data.main_info_1, *test_data.add_info_args)
denis = Contact(*test_data.main_info_2, **test_data.add_info_kwargs)
stepan = Contact(*test_data.main_info_3, *test_data.add_info_args)
ilya = Contact(*test_data.main_info_4, **test_data.add_info_kwargs)
contacts = [sacha, denis, stepan, ilya]

# инициируем экземпляр телефонной книги
book = Phonebook('Test')

# добавим в нее тестовые контакты
for contact in contacts:
    book.add_contact(contact)

# проверим работоспособность методов телефонной книги
book.print_info()
book.find_all_favorites()
book.delete_selected_contact(123456789)
book.find_by_initials('Velov')