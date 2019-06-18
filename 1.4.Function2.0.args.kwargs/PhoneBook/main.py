from func import Contact, Phonebook
import test_data

sacha = Contact(*test_data.main_info_1, *test_data.add_info_args)
denis = Contact(*test_data.main_info_2, **test_data.add_info_kwargs)
stepan = Contact(*test_data.main_info_3, *test_data.add_info_args)
ilya = Contact(*test_data.main_info_4, **test_data.add_info_kwargs)
contacts = [sacha, denis, stepan, ilya]

book = Phonebook('Test')

for contact in contacts:
    book.add_contact(contact)

book.print_info()
book.find_all_favorites()
book.delete_selected_contact(123456789)
