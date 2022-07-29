"""
Дан какой-то массив дат и привязанных к ним процентов. Нужно возвращать (отображать) процент на определенную дату.
"""

massive = {'29.07.2022': 30, '30.07.2022': 25, '31.07.2022': 35}


def date_percents(date):
    return massive[date]


print(date_percents('29.07.2022'))
print(date_percents('30.07.2022'))
print(date_percents('31.07.2022'))


def print_all_percents(massive):
    for key in massive:
        print(key, '=>', massive[key])


print_all_percents(massive)