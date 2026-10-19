import math
from abc import ABC, abstractmethod
import logging
from logging import Logger

logger = logging.getLogger()
# logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s'))
logger.addHandler(file_handler)


class Figure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Triangle(Figure, object):
    def __init__(self, side_a, side_b, side_c):
        logger.debug(f'Start init method')
        logger.log(25, "Custom level")
        if (not isinstance(side_a, (int, float)) or
                not isinstance(side_b, (int, float)) or
                not isinstance(side_c, (int, float))):
            logger.exception("Triangle sides must be a number")
            raise TypeError("Triangle sides must be a number")
        if ((side_a + side_b < side_c)
                or (side_b + side_c < side_a)
                or (side_a + side_c < side_b) or
                (side_a <= 0 or side_b <= 0 or side_c <= 0)):
            logger.exception("For input values triangle couldn't be created")
            raise ValueError("For input values triangle couldn't be created")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.__get_angles()
        logger.info(f'Created triangle with {(side_a, side_b, side_c)}')

    def __get_angles(self):
        logger.warning(f'Warning, we calculate angles')
        self._angle_a = math.atan2(self.side_a, self.side_b)
        self._angle_b = math.atan2(self.side_b, self.side_c)
        self._angle_c = math.atan2(self.side_c, self.side_a)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_square(self):
        p = 0.5 * self.get_perimeter()
        return pow(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c), 0.5)

    def __add__(self, other):
        pass


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("For input values circle couldn't be created")
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius * self.radius
