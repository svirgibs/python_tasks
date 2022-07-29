"""
Надо создать произвольный список чисел от -100 до 100 длинной в 100 чисел. Нужно вывести все числа, которые являются
результатом 0 при сложении трех чисел в списке. Вывести все варианты
"""

import random

lst = [random.randint(-100, 100) for i in range(100)]

print(lst)

for x1 in lst:
    for x2 in lst:
        for x3 in lst:
            res = x1 + x2 + x3
            if res == 0:
                print(x1, x2, x3)
