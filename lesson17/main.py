from lesson17.models import RandomList, func1, own_generator, one_more_function
from lesson8.model import Dog, Cat

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = RandomList([11, 21, 31, 41, 51, 61, 71, 81, 91])

print(l1)
print(l2)

for i in l1:
    # iterator=l1.get_iterator() -> iterator.__next__()
    print(i)

for i in l2:
    print(f'random iterations = {i}')


iterator = iter(l1)
print(f'fom not random list {next(iterator)}')

# random_iterator = iter(l2)
# for i in range(len(l2) + 1):
#     print(f'iteration={i}')
#     print(f'iteration={i} from random list {next(random_iterator)}')


# dog = Dog()
# cat = Cat()

# for i in dog:
#     print(i)

# for i in cat:
#     print(i)

gen = own_generator(10)
# print(own_generator())
# print(func())
# print(next(gen))
# print(next(gen))
# print(next(gen))
iterations = 0
for i in gen:
    iterations += 1
    print(f'random iterations = {iterations}, generated {i}')


# func = decorator(func)
print(func1())
print(one_more_function())