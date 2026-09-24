import re

str1 = '  Hello World. My Name Is Vova  {} {} smell like' #     [H,e,l,l,o, ,w,o,r,l,d]
# STR_1 =
str3 = str(10)
#                                           0 1 2 3 4 5 6 7 8 9 10
#                                          -11-10-9-8-7-6-5-4-3-2-1

print(str1)
# [ [start_index] : (end_index) : step ]
print(str1[::]) # [0:11:1]
print(str1[-5])
print(str1[:3])
print(str1[::2])
print(str1[0:-1:1])

words = str1.split('. ')
print(words)

print(len(str1))

# print(str1.index('x'))
print(str1.find('x'))
print(str1.index('W'))
print(str1.find('W'))
print(str1.rfind('W'))
print(str1.count('o'))
print(str1.startswith("H"))
print(str1.endswith("."))
print(str1.islower())
print(str1.istitle())

str2 = str1.upper()
print(str2)
print(str1)
print(str1.lower())
# print(str1.title())
print(str1)

# str1[0] = "K"
print(str1.swapcase())

print(str1.replace('World', 'Mike'))

print(str1.strip())

print(str1 + "!" + str2)
print("{}".join([str1, str2, str2, str2, str1]))
print("{}".join(str1))
print(f'We have str1 with value={str1} and str2 with value = {str2}')
print(str1.format('value1', 'value2'))

number = 10
string_number = str(number)
print(number)
print(string_number)
print(string_number.__class__)
print(string_number + str(1))
second_number = float(string_number)
print(f'second_number={second_number:.2f}')

findings = re.findall(r'[A-Z]\w+[ |\.]', str1)
print(findings)
print(len(findings))
print(str1.index('mell'))

print(re.findall(r'([A-Z]\w+)[ |\.]', str1))
print(sum(1 for i in str1.split() if i.istitle()))
print(sum(len(i.rstrip()) for i in re.findall(r'([A-Z]\w+)[ |\.]', str1)))
# sum()
# any()
# all()