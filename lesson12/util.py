from lesson12.model import Circle, Triangle


def is_circle_inside_triangle(circle: Circle, triangle: Triangle, default_arg=True, *args, **kwargs):
    # print(circle.radius)
    return circle.radius == 2 * triangle.get_square() / triangle.get_perimeter()


def foo():

    def another_foo():
        return True

    another_foo()

print(foo())