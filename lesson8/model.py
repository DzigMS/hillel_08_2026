from abc import ABCMeta, ABC
from datetime import datetime
from urllib.request import Request

COLORS = ['red', 'green', 'blue', 'ocean', 'yellow']
BRANDS = ['BMW', 'Mercedes', 'Ferrari', 'Maclaren', 'ZaZ']


class Car:
    # brand = "Mercedes"
    def __init__(self, brand_name: str, color: str, dob: datetime=datetime.now()):
        self._brand = brand_name
        # if brand_name == 'Ferrari':
        #     self.color = 'red'
        # else:
        #     self.color = color
        self.__color = 'red' if brand_name == 'Ferrari' else color

        self.__dob = dob
        self.is_started = False
        print(f"Create a new car with brand {brand_name}")

    def __del__(self):
        print(f'Delete car with {self._brand}')

    def get_color(self):
        return self.__color

    def get_dob(self):
        return self.__dob

    def get_age(self, date = datetime.now()):
        return date - self.__dob
    def __repr__(self):
        return f"Car {self._brand} {self.__color} {self.__dob}"

    # def __setattr__(self, key, value):
    #     pass
    # def __getattr__(self, item):
    #     pass

    def __add__(self, other):
        if not isinstance(other, Car):
            return None
        return Car(f'{self._brand} {other._brand}', 'magic', min(self.__dob, other.__dob))

    def __sub__(self, other):
        if not isinstance(other, Car):
            return None
        return f'sub between {self} and {other}'

    # def __iter__(self):
    #     return range

    def start(self):
        if not self.is_started:
            self.is_started = True
        return self.is_started

    def stop(self):
        if self.is_started:
            self.is_started = False
        return self.is_started


class Speaker:
    pass

class Display:
    pass

class Phone:
    def __init__(self, speaker: Speaker, microphone, form_factor):
        self.speaker = speaker
        self.microphone = microphone
        self.form_factor = form_factor

    def call_to(self, phone_number):
        # self.speaker.turn_on()
        print(f'Call processing to phone_number {phone_number}')

    def call_from(self):
        print(f'Income call')

    def ring(self):
        pass

class MobilePhone(Phone):
    def __init__(self, speaker: Speaker, microphone):
        super().__init__(speaker, microphone, 'mobile')
        self.display = Display()

    def reject_income(self):
        pass


class Animal(ABC):
    def common_method(self):
        print('Common method')

    def voice(self):
        print('Voice from Animal')


class Cat(Animal):
    def voice(self):
        print('Meow')

    # def common_method(self):
    #     print('Common method')


class Elephant(Animal):
    pass

class Dog(Animal):
    def voice(self):
        print('Woof')

    # def common_method(self):
    #     print('Common method')

class Reptiloid:
    def change_skin(self):
        print('Change Skin')

    def voice(self):
        print('I am Reptiloid')


class Snake(Animal, Reptiloid):
    def voice(self):
        Reptiloid.voice(self)


class Vasilisk(Snake):
    def some_method(self):
        pass
