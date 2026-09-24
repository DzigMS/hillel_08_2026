import math
import sys

first_number = 2 # int(2)
second_number = int(3)
float_number = 3.555777
float_number2 = float('7.3') # 7.3
str1 = 'a'
str3 = str1
str2 = str('b')

print(str1.__class__)
print(second_number.__class__)

# + - * / > < >= <= != == >> << // % **

print(first_number)
first_number = first_number << 3 # 2**3 pow(2,3)
print(first_number)
# math.sqrt()

print(float_number)
a = 0.3333333333333333
print(2/3 + a)
biiiiig_number = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(biiiiig_number)
print(sys.getsizeof(biiiiig_number))
print(sys.getsizeof(first_number))
print(sys.getsizeof(float_number2))
print(sys.getsizeof(float_number))
print(sys.getsizeof(61.74737383891932934932048573457239514950295323532453345325532515435325365634654643646464564564564564564645646464646464564599999999999999999999999999999999999999999999999999999999999999999999999999999999))

# and or
first_bool = (first_number > float_number2)
second_bool = False
print((first_bool and second_bool) or True)
print(first_bool or second_bool)

# collection (list, set, tuple, dict) / sequences
# None

name = input("What is your name\n")
# age_input = input("How old are you?\n")
age = int(input("How old are you?\n"))
print(type(name))
print(type(age))
print(f'name is {name}, age is {age}')

# str_tuple = tuple(str3)
# print(str_tuple)

