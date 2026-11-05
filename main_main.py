import modulefinder

from requests import Request

from lesson16.module import foo, Foo
from lesson16.another_module import func1


if __name__ == '__main__':
    print("Start program")
    foo()
    func1()
    f = Foo()
    Request()