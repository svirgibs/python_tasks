"""
Дана строка st = "one two three four one five one three two six".
Нужно вывести все повторяющиеся слова на консоль.
"""

# строка с повторами слов
st = "one two three four one five one three two six"


# Решение
st_lst = st.split(" ")
final_lst = []
index = 0

while index < len(st_lst):
    if st_lst.count(st_lst[index]) > 1:
        if st_lst[index] not in final_lst:
            final_lst.append(st_lst[index])
    index += 1

# Вывод результата
print(final_lst)

