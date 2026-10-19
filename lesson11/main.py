from lesson11.model import OwnError

value_error = OwnError('We just play with exceptions')
# print(value_error)

def func1():
    print('func1 start')
    try:
        func2()
    except ValueError as e:
        print("Value error catcher")

    print('end func1')

def func2():
    print('func2 start')
    try:
        func3()
    except ArithmeticError as e:
        print('Catch ArithmeticError only')
        print(e)

    # func3()
    print('end func2')

def func3():
    print('func3 start')
    print(value_error)
    raise value_error
    print('end func3')

try:
    func1()
except ValueError as e:
    print("catch everything")

# try except, try except except ..., try except... finally, try finally, try except else

def divide(a, b):
    if b == 0:
        return "Divide by zero is mathematics unresolved"
    return a/b

try:
    # raise ValueError
    print('try block')
except ZeroDivisionError:
    print('Are you stupid divide by zero')
else:
    print('Else block')
finally:
    print("Always Coca-Cola")