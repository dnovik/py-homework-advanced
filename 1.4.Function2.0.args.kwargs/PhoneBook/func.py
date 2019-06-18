class Contact:
    
    def __init__(self, name, surname, phone_number, favorite=False, *args, **kwargs):

        def is_favorite(status):
            if status == True:
                return 'Да'
            else:
                return 'Нет'
        
        self.contact_info = {
            'main' : {},
            'add' : {}
            }

        self.contact_info['main']['Имя'] = name
        self.contact_info['main']['Фамилия'] = surname
        self.contact_info['main']['Телефон'] = phone_number
        self.contact_info['main']['В избранных'] = is_favorite(favorite)

        if args:
            try:
                self.contact_info['add']['Email'] = args[0]
                self.contact_info['add']['Telegram'] = args[1]
                self.contact_info['add']['VK'] = args[2]
                self.contact_info['add']['Доп.телефон 1'] = args[3]
                self.contact_info['add']['Доп.телефон 2'] = args[4]
            except IndexError:
                pass

        elif kwargs:
            try:
                self.contact_info['add']['Email'] = kwargs.get('email', ' ')
                self.contact_info['add']['Telegram'] = kwargs.get('telegram', ' ')
                self.contact_info['add']['VK'] = kwargs.get('vk', ' ')
                self.contact_info['add']['Доп.телефон 1'] = kwargs.get('add_phone_1', ' ')
                self.contact_info['add']['Доп.телефон 2'] = kwargs.get('add_phone_2', ' ')
            except KeyError:
                pass

    
    def __str__(self):
        
        return f"Name: {self.contact_info['main']['Имя']}" + '\n' + f"Surname: {self.contact_info['main']['Фамилия']}" + '\n' + f"Phone: {self.contact_info['main']['Телефон']}" + '\n' + f"Favotite: {self.contact_info['main']['В избранных']}" + '\n' + 'Additional info:' + '\n' + '\t' + f"Email: {self.contact_info['add'].get('Email')}" + '\n' + '\t' + f"Telegram: {self.contact_info['add'].get('Telegram')}" + '\n' + '\t' + f"VK: {self.contact_info['add'].get('VK')}" + '\n' + '\t' + f"Phone add 1: {self.contact_info['add'].get('Доп.телефон 1')}" + '\n' + '\t' + f"Phone add 2: {self.contact_info['add'].get('Доп.телефон 2')}"



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
            if contact.contact_info['main']['В избранных'] == 'Да':
                print(contact)

    def delete_selected_contact(self, phone_num):
        for contact in self.book:
            if contact.contact_info['main']['Телефон'] == str(phone_num):
                self.book.remove(contact)

    def find_by_initials(self):
        pass