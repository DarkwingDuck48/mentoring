
def square_def(x):
    return x ** 2

print(square_def(5))


square_lambda = lambda x: x ** 2  # noqa: E731

print(square_lambda(5)) # Вывод: 25

students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 85},
    {'name': 'Charlie', 'grade': 95}
]

sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Вывод: [2, 4, 6]


squares = list(map(lambda x: x ** 2, numbers))
print(squares) # Вывод: [1, 4, 9, 16, 25, 36]

words = ['apple', 'banana', 'cherry']
sorted_by_last_letter = sorted(words, key=lambda word: word[-1])
print(sorted_by_last_letter) # Вывод: ['banana', 'apple', 'cherry'] (a, e, y)