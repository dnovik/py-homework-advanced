import re
from pprint import pprint
import csv

# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


initial_pat = r'^([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)\s?\,?([а-яёА-ЯЁ]*)([а-яёА-ЯЁ]*)\,*([а-яёА-ЯЁ]*)\,*'
phone_pat = r'(\+7|8)\s?\(?(\d{3})\)?\s?\)?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?(\(?[а-яёА-ЯЁ]*\.\s)?(\d{4})?'
email_pat  = r'(\w+\.?\w+@\w*\.\w*)'



text = []
phone_list = []
initial_list = []
email_list = []

for contacts in contacts_list[1:]:
    text.append(','.join(contacts))

for line in text:
  inits = re.findall(initial_pat, line)
  phones = re.findall(phone_pat, line)
  emails = re.findall(email_pat, line)


  for init in inits:

      lastname = init[0]
      firstname = init[1]
      thirdname = init[2]
      organization = init[4]

      initial_list.append([lastname, firstname, thirdname, organization])


  if len(phones) == 1:
    for phone in phones:
                country_code = re.sub(r'\+7|8', '+7', phone[0])
                add = re.sub(r'\(?\доб\.\s?', 'доб.', phone[5])
                phone_num = f'{country_code}({phone[1]}){phone[2]}-{phone[3]}-{phone[4]} {add} {phone[6]}'
                phone_list.append(phone_num)
  else:
        phone_num = ''
        phone_list.append(phone_num)
  
  if len(emails) == 1:
        for email in emails:
              email_list.append(email)
  else:
        email = ''
        email_list.append(email)

data = []
            
for line in initial_list:
      data.append(line)

a = list(zip(data, phone_list, email_list))

book = {}

for i in a:
  lastname = i[0][0]
  firstname = i[0][1]
  thirdname = i[0][2]
  organization = i[0][3]
  phone = i[1]
  email = i[2]
  

  if lastname not in list(book.keys()):
        book[lastname] = {
            'lastname' : lastname,
            'firstname' : firstname,
            'thirdname' : thirdname,
            'organization' : organization,
            'phone' : phone,
            'email' : email
        }
  elif lastname in list(book.keys()):
        if book[lastname]['thirdname'] == '':
          book[lastname]['thirdname'] = thirdname
        elif book[lastname]['organization'] == '':
              book[lastname]['organization'] = organization
        elif book[lastname]['phone'] == '':
              book[lastname]['phone'] = phone
        elif book[lastname]['email'] == '':
              book[lastname]['email'] = email


for v in book.values():
  print(v)