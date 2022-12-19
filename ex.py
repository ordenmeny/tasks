#  Создать список из n чисел.
#  Найти количество пар, сумма которых простое число и минимальную такую сумму. Ответ перевести в семеричную С/Сч
from random import randint

lst = [randint(1, 100) for i in range(1, 100)]


def func(enum):
    sum_s = lst[enum[0]] + lst[enum[0] + 1]
    if sum_s == 2:
        return lst[enum[0]], lst[enum[0] + 1]
    if not (any(map(lambda x: sum_s % x == 0, range(2, sum_s)))):  # проверяет, простое ли число
        return lst[enum[0]], lst[enum[0] + 1]  # если да, то возвращает элементы по индексу списка lst
    return None


def rotate(n):
    st = ''

    while n // 7 != 0:
        st = str(n % 7) + st
        st = str(n // 7) + st
        n //= 7
    return st if st != '' else n


res = rotate(min(map(lambda x: sum(x), filter(lambda x: x, map(func, enumerate(lst[:-1]))))))
print(res)
