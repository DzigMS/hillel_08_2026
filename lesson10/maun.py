'''
Створіть глобальну змінну, яка зберігає кількість створених об'єктів.
Напишіть клас «Користувач» з приватними властивостями «ім'я» та «email», які ініціалізуються через конструктор.
При створенні кожного користувача глобальний лічильник має збільшуватись на 1.
Створіть кілька користувачів і виведіть у консоль їх загальну кількість.
Потім перепишіть рішення так, щоб лічильник зберігався в атрибуті класу, а не в глобальній змінній,
і поясніть у коментарі, чим відрізняються ці підходи.
'''
from lesson10 import constants
from lesson10.model import User, Student

user1 = User('Mike', 'email@email.com')
print(f'count user after Mike {User.get_user_count()}')
user2 = User('Vova', 'vovan@gmail.com')
print(f'count user after Vova {User.get_user_count()}')


print(user1.get_name())
print(User.get_name(user1))
print(user1.get_user_count())

print(constants.OBJECT_COUNT)

# from lesson10.constants import OBJECT_COUNT # OBJECT_COUNT = constants.OBJECT_COUNT
# print(OBJECT_COUNT)
# OBJECT_COUNT += 1
# print(OBJECT_COUNT)

# print(type(OBJECT_COUNT))
# print(type(constants))
# print(type(lesson3))

st1 = Student('Nastia', 'nastia@gmail.com')
print(f'user count = {User.get_user_count()}')
print(f'User count {User.class_method()}')
print(f'objects count = {constants.OBJECT_COUNT}')
print(f'Student count {Student.class_method()}')
print(f'Student count2 {Student.get_user_count()}')

print(Student.mro())

user1.any_new_field = 100
print(user1.any_new_field)
# print(user2.any_new_field)
