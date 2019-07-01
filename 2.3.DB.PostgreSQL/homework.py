import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import sql

db_name = 'test'
db_user = 'user'
db_pass = 'pass'

student_1 = {'name' : 'Petr', 'gpa' : 4.5, 'birth' : '2001-01-13'}

students = [
    {'name' : 'Igor', 'gpa' : 4.3, 'birth' : '2012-01-13'},
    {'name' : 'Oleg', 'gpa' : 4.2, 'birth' : '1901-01-13'},
    {'name' : 'Fedor', 'gpa' : 4.7, 'birth' : '2201-01-13'},
    {'name' : 'Svetlana', 'gpa' : 5, 'birth' : '2031-01-13'}
]


students = ("id serial PRIMARY KEY", "name varchar(100)",
    "gpa numeric(10,2)", "birth date")

courses = ("id serial PRIMARY KEY", "name varchar(100)")

student_course = ("id serial PRIMARY KEY", "student_id INTEGER REFERENCES students(id)", "course_id INTEGER REFERENCES courses(id)")


class DataBase:

    def __init__(self, db_name, db_user, db_pass, host='localhost'):
        
        self.db_name = db_name
        self.db_user = db_user
        self.host = host
        self.db_pass = db_pass

        try:
            self.conn = psycopg2.connect(dbname=self.db_name, user=self.db_user, password=self.db_pass, host=self.host)
            self.conn.autocommit=True
            self.cursor = self.conn.cursor()
        except:
            print("Can't connect to the database")

        

    # создает таблицы
    def create_db(self, table_name, fields): 
        
        query = "CREATE TABLE {} ({});".format(table_name, ",".join(fields))

        self.cursor.execute(query)
        

    # возвращает студентов определенного курса
    def get_students(self, course_id): 
        pass

    # создает студентов и записывает их на курс
    def add_students(self, course_id, students): 
        pass

    # просто создает студента
    def add_student(self, student): 
        
        query = "INSERT INTO students(name, gpa, birth) VALUES(%(name)s, %(gpa)s, %(birth)s);"

        self.cursor.execute(query, student)

    def get_student(self, student_id):

        query = "SELECT * FROM students WHERE students.id = {}".format(student_id)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        return result
        



if __name__ == "__main__":    
    database = DataBase(db_name, db_user, db_pass)




