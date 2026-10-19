import unittest
from unittest import TestCase
from unittest.mock import Mock

from lesson12.model import Triangle, Circle, Figure
from lesson12.util import is_circle_inside_triangle


# def test():
#     # given
#     expected_result = 1
#     number_1 = 2
#     number_2 = 2
#
#     # when
#     # call test function
#     actual_result = divmod(number_2, number_1)
#
#     # then
#     assert actual_result == expected_result


class TheoryTest(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUp before all tests")

    @classmethod
    def tearDownClass(cls):
        print("tearDown after all tests")

    def setUp(self):
        # raise ValueError
        print('Before each test')

    def tearDown(self):
        print('After each test')

    def test_first(self):
        print('Run first test')
        # self.assertEqual

    def test_second(self):
        print('Run second test')


class TriangleTest(TestCase):
    def test_constructor(self):
        valid_sides = [(10, 10, 10), (2, 3, 4), (100, 50, 50)]
        # a, b, c = 10, 10, 10

        for a, b, c in valid_sides:
            with self.subTest(f'side a: {a}, side b: {b}, side c: {c}'):
                actual = Triangle(a, b, c)
                # actual = Circle(a)
                self.assertEqual(actual.side_a, a)
                self.assertEqual(actual.side_b, b)
                self.assertEqual(actual.side_c, c)
                self.assertIsInstance(actual, Triangle)
                self.assertIsInstance(actual, Figure)
                self.assertEqual(actual.__class__, Triangle)
                # self.assertEqual(actual.__class__, Figure)

    def test_constructor_with_value_error(self):
        invalid_sides = [(10, 1, 3), (2, 3, 6), (100, 50, 25)]
        # a, b, c = 10, 1, 3

        for a, b, c in invalid_sides:
            with self.subTest(f'side a: {a}, side b: {b}, side c: {c}'):
                with self.assertRaises(ValueError) as e:
                    Triangle(a, b, c)
                self.assertEqual("For input values triangle couldn't be created", e.exception.args[0])



class UtilTest(TestCase):
    def test_is_circle_inside_triangle(self):
        circle = Mock(spec=Circle)
        circle.radius = 10
        triangle = Mock(spec=Triangle)
        triangle.get_square.return_value = 20
        triangle.get_perimeter.return_value = 5
        # circle = Circle(10)
        # triangle = Triangle(12, 10, 1)

        actual = is_circle_inside_triangle(circle, triangle)
        self.assertFalse(actual)


if __name__=="__main__":
    unittest.main()