"""
Дано 2 списка a = [1, 2, 3] и b = [4, 5, 6]. Нужно вывести новый список используя a и b, c = [1, 2, 3, 4, 4, 5, 6]
"""

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b[:1] + b

print(c)