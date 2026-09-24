# object
import random
from datetime import datetime

from lesson8.model import Car, COLORS, BRANDS

first_car = Car("BMW", 'red', datetime(2023, 12, 3))
print(f"after create first car {first_car._brand}")
second_car = Car("Mercedes", 'green')

print(f'first car {first_car._brand}, {first_car.__color}, {first_car.__dob}')
print(f'second car {second_car._brand}, {second_car.__color}, {second_car.__dob}')
# first_car
print(type(first_car))
# del first_car
print(f'After delete car {first_car._brand}')

def generate_car_list(count=10):
    cars = []
    for i in range(count):
        color = COLORS[random.randint(0, len(COLORS) - 1)]
        brand = BRANDS[random.randint(0, len(BRANDS) - 1)]
        cars.append(Car(brand, color))
    return cars

print(generate_car_list(5))

print(f'state {first_car.is_started}')
first_car.start()
print(f'state {first_car.is_started}')
first_car.stop()
print(f'state {first_car.is_started}')
