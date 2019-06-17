

main_info = ['Denis', 'Novik', '123456789']

add_info_args = ['dnovik@grundfos.com', 'dnovik@grundfos.com', '@dnovik', 'vk.dnovik', '123456789_1', '1234_2']

add_info_kwargs = {
    'email' : 'dnovik@grundfos.com', 
    'telegram' :'@dnovik', 
    'vk' :'vk.dnovik',
    'add_phone_2' : '1234_2',
    'add_phone_1' : '123456789_1'}

class Contact:

    def __init__(self, name, surname, phone_number, favorite=False, *args, **kwargs):
        
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite

        try:
            self.email = args[0]
            self.telegram = args[1]
            self.vk = args[2]
            self.add_phone_1 = args[3]
            self.add_phone_2 = args[4]
        except IndexError:
            pass

        try:
            self.email = kwargs['email']
            self.telegram = kwargs['telegram']
            self.vk = kwargs['vk']
            self.add_phone_1 = kwargs['add_phone_1']
            self.add_phone_2 = kwargs['add_phone_2']
        except KeyError:
            pass


    def __str__(self):

        return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}' + '\n' + f'Телефон: {self.phone_number}' + '\n' + f'В избранных: {self.favorite}' + '\n' + 'Дополнительная информация:' + '\n' + '\t' + f'E-mail: {self.email}' + '\n' + '\t' + f'Telegram: {self.telegram}' + '\n' + '\t' + f'VK: {self.vk}' + '\n' + '\t' + f'Доп.телефон 1: {self.add_phone_1}' + '\n' + '\t' + f'Доп.телефон 2:{self.add_phone_2}'


contact = Contact(*main_info)
print(contact)


#2. класс PhoneBook:
# - Название телефонной книги - обязательное поле;
# - Телефонная книга должна работать с классами Contact.
# Методы:
# - Вывод контактов из телефонной книги;
# - Добавление нового контакта;
# - Удаление контакта по номеру телефона;
# - Поиск всех избранных номеров
# - Поиск контакта по имени и фамилии


class Phonebook:

    def __init__(self, name):
        self.name = name
        self.book = list()

    def add_contact(self, contact):
        self.book.append(contact)

    def print_info(self):
        for contact in self.book:
            print(contact)

    def find_all_favorites(self):
        for contact in self.book:
            if contact.favorite == True:
                print(contact)

    



phonebook = Phonebook('Test')
denis = Contact(*main_info, favorite=True, **add_info_kwargs)
oleg = Contact('Oleg', 'Popov', '12334456', favorite=True)
phonebook.add_contact(oleg)
phonebook.print_info()