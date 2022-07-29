"""
    Дана строка. Нужно развернуть ее в обратную сторону 2мя способами
"""

default_string = "Hello, world!"

# Первый способ
reversed_string_1 = default_string[::-1]
print("Первый способ [::-1]: %s" % reversed_string_1)

# Второй способ
reversed_string_2 = ''.join(reversed(default_string))
print("Второй способ ''.join(reversed()): %s" % reversed_string_2)


# Функция разворачивающая любую строку
def reverse_string(string):
    return string[::-1]


print("Функция reverse_string(): %s" % reverse_string('Python'))
