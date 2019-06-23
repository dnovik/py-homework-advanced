import re
from pprint import pprint
import csv

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


initials = r'^([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)([а-яёА-ЯЁ]*)\,*([а-яёА-ЯЁ]*)\,*'

phones = r'(\+7|8)\s?\(?(\d{3})\)?\s?\)?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?(\(?[а-яёА-ЯЁ]*\.\s)?(\d{4})?'

emails  = r'(\w+\.?\w+@\w*\.\w*)'


book = []
for contacts in contacts_list[1:]:
    contact = ','.join(contacts)
    print(re.findall(phones, contact))

    



