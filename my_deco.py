import time
from functools import wraps


def my_timer(func):
    @wraps(func)
    def wrap(*args, **kwrgs):
        start_time = time.time()
        result = func(*args, **kwrgs)
        delta_time = time.time() - start_time
        print(f'Время выполнения функции {delta_time}')
        return result

    return wrap


def logging(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('my_file.txt', 'a', encoding= 'UTF-8') as f:
            start_time = time.ctime()
            f.writelines(
                f'\nfunction name: {func.__name__} with result = {result}. Start at {start_time}'
            )
            return result

    return wrap


@logging
@my_timer
def my_sum(x, y, z):
    return x+ y **z


print(my_sum(4, 5, 7))



