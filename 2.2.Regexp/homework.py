import re
from pprint import pprint
import csv

# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# находим регулярные выражения для ФИО + организация, телефонов, эл.адресов
initial_pat = r'^([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)([а-яёА-ЯЁ]*)\,*([а-яёА-ЯЁ]*)\,*'
phone_pat = r'(\+7|8)\s?\(?(\d{3})\)?\s?\)?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?(\(?[а-яёА-ЯЁ]*\.\s)?(\d{4})?'
email_pat  = r'(\w+\.?\w+@\w*\.\w*)'

initial_list = []
phone_list = []
email_list = []

# кладем результат работы регулярок в соответствующие списки
for contacts in contacts_list[1:]:
      contact = ','.join(contacts)
      initials = re.findall(initial_pat, contact)
      initial_list.append(initials)
      phones = re.findall(phone_pat, contact)
      phone_list.append(phones)
      emails = re.findall(email_pat, contact)
      email_list.append(emails)

# объединяем данные для дальнейшей работы
raw_data = list(zip(initial_list, phone_list, email_list))

# создаем словарь в который по ключам разложим данные
book = {}

for info in raw_data:
      lastname = info[0][0][0]
      firstname = info[0][0][1]
      thirdname = info[0][0][2]
      organization = info[0][0][4]
      phones = info[1]
      emails = info[2]
      
      # корректируем формат телефонов
      for phone in phones:
            country_code = re.sub(r'\+7|8', '+7', phone[0])
            add = re.sub(r'\(?\доб\.\s?', 'доб.', phone[5])
            if add:
                  phone_num = f'{country_code}({phone[1]}){phone[2]}-{phone[3]}-{phone[4]} {add} {phone[6]}'
            else:
                  phone_num = f'{country_code}({phone[1]}){phone[2]}-{phone[3]}-{phone[4]}'
      
      # собираем эл.адреса
      if len(emails) == 1:
            for email in emails:
                  email = email
      else:
            email = ''

      # кладем данные в словарь и избавляемся от дублей
      if lastname not in list(book.keys()):
            book[lastname] = {
            'lastname' : lastname,
            'firstname' : firstname,
            'thirdname' : thirdname,
            'organization' : organization,
            'phone' : phone_num,
            'email' : email
        }
      elif lastname in list(book.keys()):
            if book[lastname]['thirdname'] == '':
                  book[lastname]['thirdname'] = thirdname
            elif book[lastname]['organization'] == '':
                  book[lastname]['organization'] = organization
            elif book[lastname]['phone'] == '':
                  book[lastname]['phone'] = phone_num
            elif book[lastname]['email'] == '':
                  book[lastname]['email'] = email

# приведем результат к первоначальному виду


fields = list(list(book.values())[0].keys())
info = []

for value in list(book.values()):
      if fields not in info:
            info.append(fields)
      info.append(list(value.values()))

for line in info:
      if '' in line:
            line.remove('')


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f)
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(info)


