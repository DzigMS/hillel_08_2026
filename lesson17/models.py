import random


class RandomIterator:
    def __init__(self, objects):
        self.list = objects
        self.counter = 0
        self.indexes = []

    def __next__(self):
        self.counter += 1
        if self.counter > len(self.list):
            raise StopIteration

        index = random.randrange(len(self.list))
        while index in self.indexes:
            index = random.randrange(len(self.list))
        self.indexes.append(index)
        return self.list[index]


class RandomList(list):
    def __iter__(self):
        # return self
        return RandomIterator(self)

    # def __next__(self):
    #     #     return self[random.randrange(len(self))]


def decorator(another_func):
    def wrapper():
        return f'{another_func()} and hello from wrapper inside decorator'

    # return 'hello from decorator'
    return wrapper

def another_decorator(another_func):
    def wrapper():
        return f'{another_func()} and hello from decorator inside another_decorator'

    return wrapper

@another_decorator # func = another_decorator(decorator(func))
@decorator # func = decorator(func)
def func1():
    return 'hello from func'

@decorator # one_more_function = decorator(one_more_function)
def one_more_function():
    return 'hello from one more function'

def own_generator(count):
    counter = 0
    while counter < count:
        rand_int = random.randint(1, 100)
        yield rand_int
        if rand_int > 70:
            return
        counter += 1
    # yield 'first'
    # yield 'second'

