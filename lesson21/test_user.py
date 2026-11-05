import random
import uuid
from unittest import TestCase

from lesson21.models import ORMUser
from lesson21.utils import add_orm_user, get_all_users_legacy, Session


class UserTest(TestCase):
    def setUp(self):
        self.session = Session()

    def test_add_user(self):
        expected_id = uuid.uuid4()
        user = ORMUser(id=expected_id, name='test', age=random.randint(10, 70))

        add_orm_user(user)

        users = self.session.query(ORMUser).filter_by(id=expected_id).all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, expected_id)