import random

MODULE_VARIABLE = "This is module var"
# def func_name():
#   local variables
#   logic/implementation
#   return
def random_number(number_count, diapason=10, *any_name_but_default_is_args, **kwargs):
    """
    Generate number_count random numbers.
    First in diapason 0-diapason, second diapason-20 and third 20-30
    :param number_count: number of random numbers
    :return: string with numbers joined by space
    """
    # number = 0
    # number = random.randint(0, 333)
    # return number
    print(type(kwargs))
    print(kwargs)
    random_numbers = [
        str(random.randint(i*diapason, i*diapason + diapason))
        for i in range(number_count)
    ]
    random_numbers.extend([str(num) for num in any_name_but_default_is_args])
    return_str = ' '.join(random_numbers)
    return return_str


print(random_number(2, 30))
print(random_number(3))
print(random_number(3, 5, 10, 7, 33, 77, 12))
print(random_number(3, 5, some_my_var=10, another_var=7))


def own_sum(first_number, second_number, *args):
    result = 0
    for number in args:
        result += int(number)
    return int(first_number) + int(second_number) + result
    # return sum([*args, first_number, second_number])

# sum(sum(2, 3), 7)
# print(own_sum("2", 4, 6, 10, 5, '10'))
# print(sum([2, 4, 6, 10, 5, '10']))

generated_numbers = random_number(10, 20 , 120, 11, 13, 77 ,33)
print(generated_numbers)

str1 = list(MODULE_VARIABLE)
print(str1)
str1.sort(key=lambda ch: ch > 'b')
print(str1)