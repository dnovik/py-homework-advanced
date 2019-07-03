import csv
import re
from pymongo import MongoClient
from datetime import datetime


client = MongoClient()
my_database = client['Concert_App']
concert_collection = my_database['Concerts']
csv_file = 'artists.csv'


def read_data(csv_file, db):

    # прочитать файл с данными и записать в коллекцию
    concerts = list()

    with open(csv_file, encoding='utf8') as csvfile:
            
            reader = list(csv.DictReader(csvfile))
            for line in range(len(reader)):
                
                concerts.append({
                        'Исполнитель' : reader[line]['Исполнитель'],
                        'Цена' : int(reader[line]['Цена']),
                        'Место' : reader[line]['Место'],
                        'Дата' : datetime.strptime(reader[line]['Дата'] + '.' + '2019',  '%d.%m.%Y')
                        }
                )

            concert_collection.insert_many(concerts)


def find_cheapest(db):
    
    return list(db.find().sort([('Цена', 1 )]))



def find_by_name(name, db):

    regex = re.compile(f'{name}', re.I)
    result = concert_collection.find({'Исполнитель' : regex})
    return list(result.sort([('Цена', 1 )]))


if __name__ == '__main__':
    pass
```
