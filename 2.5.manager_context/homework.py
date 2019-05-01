from datetime import datetime

class OpenerFile():

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.start_time = datetime.now()

    def __enter__(self):
        self.file = open(self.file_path, self.mode)


        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        self.end_time = datetime.now()
        self.time_delta = self.end_time - self.start_time

        print(f'Время начала программы: {self.start_time}')
        print(f'Время завершения программы {self.end_time}')
        print(f'Длительность программы: {self.time_delta}')


        if exc_value:
            raise


    if __name__ == 'main':
        pass



import requests
import json 

link = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/3.1.formats.json.xml/newsafr.json'

news = requests.get(link).json()
file = r'D:\Python\Netology\2.5.manager_context\news.json'

with OpenerFile(file, 'w') as f:
    data_to_write = json.dumps(news)
    f.write(data_to_write)




