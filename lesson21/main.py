from lesson21.models import ORMUser
from lesson21.utils import Session, get_all_users_legacy

session = Session()




print(get_all_users_legacy())


orm_users = session.query(ORMUser).all()
print(orm_users)
session.add(ORMUser(id='4112391e-08de-4474-a454-fcbe070fe319', name='Vasia', age=23))
session.commit()
vasia = session.query(ORMUser).filter_by(name='Vasia').first()
print(vasia)
vasia.age = 73
session.commit()


print(session.query(ORMUser).all())
print(get_all_users_legacy())

