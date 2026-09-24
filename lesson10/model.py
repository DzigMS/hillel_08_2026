from lesson10 import constants


class User:
    __user_count = 0

    # __field__ = ('__first_name', 'email')

    def __new__(cls, *args, **kwargs):
        # print(f'new {cls} {cls.__user_count}')
        cls.__user_count += 1 # cls.__user_count = cls.__user_count + 1
        constants.OBJECT_COUNT += 1
        return super().__new__(cls)

    # method
    def __init__(self, first_name, email):
        self.__first_name = first_name # self.__setattr__(__first_name, first_name)
        # print(constants.OBJECT_COUNT)
        # User.__user_count += 1

    def get_name(self):
        return self.__first_name

    def __setattr__(self, key, value):
        # if key not in User.__field__:
        #     raise ValueError('Field %s is not defined.' % key)
        if 'email' == key and not value.contains('@'):
            raise ValueError('Email without @')
        # self.key = value
        super().__setattr__(key, value)


    @staticmethod
    def get_user_count():
        return User.__user_count

    @classmethod
    def class_method(cls):
        print(f'class = {cls}')
        return cls.__user_count

    def __del__(self):
        User.__user_count -= 1


class Student(User):
    __user_count = 0

    # def __new__(cls, *args, **kwargs):
    #     super().__new__(cls)

    def __init__(self, first_name, email):
        super().__init__(first_name, email)

    @staticmethod
    def get_user_count():
        return Student.__user_count