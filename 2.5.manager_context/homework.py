from datetime import datetime

class OpenerFile():

    def __init__(self, file_path):
        self.file_path = file_path
        self.start_time = datetime.now()

    def __enter__(self):
        self.file = open(self.file_path)

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


file = r'C:\Users\54292\Desktop\My folder\Python\Netology\2.5.manager_context\test.txt'

with OpenerFile(file) as f:
    print(f.read())





