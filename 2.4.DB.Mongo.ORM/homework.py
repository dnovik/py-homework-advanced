from sqlalchemy import create_engine, Integer, Column, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/SQL_ORM')
Session = sessionmaker(bind=engine)


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    start_at = Column(Date, nullable=False)
    tags = Column(JSONB, server_default = '[]', default=list, nullable=False)

    def __str__(self):
        return f'{self.id} {self.name} {self.start_at} {self.tags}'

    def __repr__(self):
        return f'{self.id} {self.name} {self.start_at} {self.tags}'


def create_all():
    Base.metadata.create_all(engine)

def add_course(**kwargs):
    course = Course(**kwargs)
    session.add(course)
    session.commit()


def find_course(tag_to_find='SMM'):
    query = session.query(Course)
    filtered_query = query.filter(Course.tags.has_key(tag_to_find))

    for course in filtered_query.all():
        print(course)

session = Session()
find_course()