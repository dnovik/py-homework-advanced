import psycopg2


db_name = 'yourdb_name'
db_user = 'yourusername'
db_pass = 'yourpass'


# Данные для создания одного студента
student_1 = {'name' : 'Petr', 'gpa' : 4.5, 'birth' : '2001-01-13'}

# Данные для создания нескольких студентов
students = [
    {'name' : 'Igor', 'gpa' : 4.3, 'birth' : '2012-01-13'},
    {'name' : 'Oleg', 'gpa' : 4.2, 'birth' : '1901-01-13'},
    {'name' : 'Fedor', 'gpa' : 4.7, 'birth' : '2201-01-13'},
    {'name' : 'Svetlana', 'gpa' : 5, 'birth' : '2031-01-13'}
]

# Исходные данные для создания таблиц
students_tab = ("id serial PRIMARY KEY", "name varchar(100)",
    "gpa numeric(10,2)", "birth date")
courses_tab = ("id serial PRIMARY KEY", "name varchar(100)")
student_course_tab = ("id serial PRIMARY KEY", "student_id INTEGER REFERENCES students(id)", "course_id INTEGER REFERENCES courses(id)")


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

        # получаем список id студентов
        query = """SELECT students.id, students.name, courses.name FROM student_course 
        JOIN students ON students.id = student_course.student_id
        JOIN courses ON courses.id = student_course.course_id
        WHERE student_course.course_id = %s;"""
        self.cursor.execute(query, (course_id,))
        result = self.cursor.fetchall()

        print(result)

        # делаем выборку студентов по списку id


    # создает студентов и записывает их на курс
    def add_students(self, course_id, students): 
        # 1 часть Добавляем данные в таблицу студенты
        for student in students:
            self.add_student(student)

        # 2 часть Добавляем данные в таблицу курс-студент
        # отбираем id по именам студентов
        student_ids = self.get_id_by_name(students)

        query = "INSERT INTO student_course(student_id, course_id) VALUES(%s, %s)"

        for stud_id in student_ids:
            self.cursor.execute(query, (stud_id, course_id))


    # пришлось сделать функцию для add_students (см.выше)
    def get_id_by_name(self, students):
        query = "SELECT students.id FROM students WHERE students.name = %s;"
        ids = []
        for student in students:
            name = student['name']
            self.cursor.execute(query, (name,))
            ids.append(self.cursor.fetchall()[0][0])

        return ids


    # просто создает студента
    def add_student(self, student): 
        
        query = "INSERT INTO students(name, gpa, birth) VALUES(%(name)s, %(gpa)s, %(birth)s);"

        self.cursor.execute(query, student)

    # получает студента
    def get_student(self, student_id):

        query = "SELECT * FROM students WHERE students.id = %s"
        self.cursor.execute(query, (student_id,))
        result = self.cursor.fetchall()

        return result
        
    # добавляет курс
    def add_course(self, course_name):

        query = "INSERT INTO courses(name) VALUES(%s);"
        self.cursor.execute(query, (course_name,))


if __name__ == "__main__":   
    # иниицируем подключение к базе данных    
    database = DataBase(db_name, db_user, db_pass)

    # создаем таблицы в базе
    database.create_db('students', students_tab)
    database.create_db('courses', courses_tab)
    database.create_db('student_course', student_course_tab)

    # создаем несколько курсов
    database.add_course('Первый курс')
    database.add_course('Второй курс')

    # создаем одного студента
    database.add_student(student_1)

    # создаем много студентов и записываем их на курс
    database.add_students(1, students)

    # выберем одного студента 
    database.get_student(1)

    # выберем много студентов, записанных на указанный курс 
    database.get_students(1)    
