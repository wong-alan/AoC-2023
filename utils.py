from time import time
from functools import wraps


def timed(func):
    @wraps(func)
    def with_timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'func:{func.__name__} args:[{args}, {kwargs}] took: {end-start:1.6f} sec')
        return result
    return with_timer
