from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


class User:
    def __init__(self, id, name, age):
        self.id = id,
        self.name = name
        self.age = age

    def __repr__(self):
        return 'User(id={}, name={}, age={})'.format(self.id, self.name, self.age)


Base = declarative_base()

class ORMUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # rel = relationship("RelatedClass")

    def __repr__(self):
        return f'id={self.id}, name={self.name}, age={self.age}'

    # def __eq__(self, other):
    #     return self.name == other.name and self.age == other.age