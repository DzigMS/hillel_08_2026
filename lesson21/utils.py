import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lesson21.models import User

connection = psycopg2.connect(
    host='localhost',
    port=5678,
    database='postgres',
    user='postgres',
    password='password'
)
engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5678/postgres')
Session = sessionmaker(bind=engine)

def get_all_users_legacy():
    cursor = connection.cursor()
    cursor.execute('select * from public.user')
    rows = cursor.fetchall()
    return [User(id=row[0], name=row[1], age=row[2]) for row in rows]

def add_orm_user(user):
    session = Session()
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        print(f'catch exception {e}')
    finally:
        session.close()