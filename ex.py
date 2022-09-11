from time import time
from sys import getsizeof


def decorator(func):
    def wrapper(*args, **kwargs):
        st = time()
        res = func(*args, **kwargs)
        et = time()
        print(f'Result: {res}, Time: {et - st}, Memory: {getsizeof(res)}')

    return wrapper


@decorator
def func(N):
    N += 1
    return sum(range(1, N))

func(10000000)
