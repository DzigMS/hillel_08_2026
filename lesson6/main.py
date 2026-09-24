# for-i for(start position, condition, increase rule)
# for each
for i in range(10):
    print(i)

numbers = [1, 3, 10, 7, 3, 2, 5]
for i in numbers:
    print(i)

a, b, c = 1, 2, 3
numbers_dict = {f'key_{i}':i for i in numbers}
for i in numbers_dict.items():
    k = i[0]
    v = i[1]
    print(i)
    print(type(i))
    print(f'key is {i[0]} and value is {i[1]}')

for k, _ in numbers_dict.items():
    print(f'key is {k} and value is {_}')

# while condition:
counter = 0
while counter < 10:
    counter += 1
    print(counter)

while True:
    if counter < 15:
        counter += 1
        # continue
    else:
        print(counter)
        break

print(counter)
    # break


# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             pass

# if    if-else  if-elif-else
if counter < 15:
    print("Counter is lower then 15")


number = int(input("Dai chislo\n"))
if number < 10:
    print('Number is lower then 10')
else:
    print('Number is bigger then 10')

if number < 18:
    print("You are young")
elif 18 < number < 25:
    print("You are middle")
elif number < 55:
    print("Go to work")
elif 100 > number > 55:
    print("Time to retire")
else:
    print("You are so old")
