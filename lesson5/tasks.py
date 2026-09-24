"""
Дано матрицю (список списків) matrix = [[1,2,3],[4,5,6],[7,8,9]].
Виведіть транспоновану матрицю.
Знайдіть суму елементів на головній діагоналі.
Знайдіть суму всіх елементів матриці.
"""


matrix = [[1,2,3],[4,5,6],[7,8,9]]

sum_of_diagonal = sum([matrix[i][i] for i in range(len(matrix))])
print(sum_of_diagonal)
sum_of_all_elements = sum([sum(row) for row in matrix])
print(sum_of_all_elements)

transparent_matrix = [[], [], []]
for row in matrix:
    for i in range(len(row)):
        transparent_matrix[i].append(row[i])

print(transparent_matrix)

transparent_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
print(transparent_matrix)


"""
students = [("Іван", 21, "ІТ"), ("Марія", 23, "Дизайн"), ("Олег", 20, "ІТ")]
За допомогою comprehension з розпакуванням for name, age, spec in students виведіть рядки f"{name} ({age}) — {spec}".
Створіть словник {ім'я: вік} через dict comprehension: {name: age for name, age, _ in students}.
"""
students = [("Іван", 21, "ІТ"), ("Марія", 23, "Дизайн"), ("Олег", 20, "ІТ")]
# for t in students:
#     print(f"{t[0]} ({t[1]}) — {t[2]}")
st_d = {}
for name, age, spec in students:
    print(f"{name} ({age}) — {spec}")
    st_d[name] = age

print(st_d)

strings = [f"{name} ({age}) — {spec}" for name, age, spec in students]
print(strings)

students_dict = {name: age for name, age, _ in students}
print(students_dict)
