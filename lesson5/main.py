# Collections
# Tuple, List, Set, Dict
from pickletools import string1

# Tuple
str1 = "abcfsadfsfa"

first_tuple = (1, 2, 5, 10, "str1", False, 5)
second_tuple = tuple(str1)
print(first_tuple)
print(second_tuple)

print(first_tuple[0])
print(first_tuple[5])
# first_tuple[1] = 7
# first_tuple[0].name = 'Maclaren'
print(first_tuple)

print(first_tuple[3: 7: 2])
print(first_tuple.index(True))

# a, b, c = 1, 2, 3
# second_tuple (a, b, c)
a, b, c = second_tuple[0:3] # a = second_tuple[0], b = second_tuple[1], c = second_tuple[2]
print(f'a={a}, b={b}, c={c}')


# List
print("List")
first_list = [7, 10, 'str2', True]
second_list = list(first_tuple)
third_list = list(str1)

print(first_list)
print(second_list)
print(third_list)

first_list.sort()
sorted(first_list)

print(first_list[2])
second_list[3] = 'False'
second_list.append(33)
second_list.insert(3, 77)
second_list.extend(first_list)
print(second_list)


first_set = {'1', 2, 3, 'hello', 1, '1'}
second_set = set(first_tuple)

print(second_set)
print(first_set)
print(first_set.pop())
print(first_set)
print(first_set.pop())
print(first_set)
first_set.add(10)
print(first_set)


first_dict = {
    'str1': string1,
    'first_list': first_list,
    'set': first_set,
    5: first_tuple
}
second_dict = dict()
print(first_dict)

print(f'get from dict by key "set"={first_dict.get("set")}')
print(f'get from dict by key "set"={first_dict["set"]}')

print(f'get from dict by unknown key {first_dict.get("unknown", "Default")}')
# print(f'get from dict by unknown key {first_dict["unknown"]}')

first_dict['any_object'] = "New Value"
print(first_dict)
# first_dict.update([5, "newValue"], )
print(first_dict)

# comprehension
generated_list = [i for i in range(1, 11) if i%2==0]
# g_l = []
# for i in range(10):
#     if i%2 == 0:
#         g_l.append(i)
print(generated_list)
generated_set = {i for i in range(1, 11) if i%2==0}
print(generated_set)
generated_dict = {f'key_{i//2}':i for i in range(1, 11) if i%2==0}

# gd = {}
# for i in range(1, 11):
#     if i%2 == 0:
#         gd[f'key_{i//2}'] = i
print(generated_dict)
print(111//4)
print(111/4)
print(first_dict.keys())
print(first_dict.values())
# first_dict.items()