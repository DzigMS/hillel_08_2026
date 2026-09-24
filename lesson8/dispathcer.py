from datetime import datetime

from lesson8.model import MobilePhone, Speaker, Car, Cat, Dog, Elephant, Snake, Vasilisk, Animal

# mobile_phone = MobilePhone(Speaker(), 'micro')
# mobile_phone.ring()

# car = Car('Ferrari', 'green', datetime(2003, 11, 23))
# print(car)
# # car.__color = 'blue'
# print(car.get_color())
#
# print(car.get_dob())
# print(car.get_age())
# print(car.get_age(datetime(2002, 10, 7)))
#
# car2 = Car('Mercedes', 'green')
#
# print(f'sub = {car2 - car}')
# print(car2 + car)
# print(f'sum of car and other object {car2 + "any string"}')

# for i in car:
#     print(i)

cat = Cat()
dog = Dog()

animals = [cat, dog, Cat(), Cat(), Dog(), Elephant(), Snake()]
for animal in animals:
    animal.voice()
    animal.common_method()

snake = Snake()
snake.change_skin()
snake.voice()

vas = Vasilisk()
vas.voice()
vas.common_method()
vas.change_skin()

an = Animal()
an.voice()
