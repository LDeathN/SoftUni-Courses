# First Problem

def logged(decorated_func):
    def decorator(*args, **kwargs):
        result = decorated_func(*args, **kwargs)
        return f"you called {decorated_func.__name__}{args}" + "\n" + f"it returned {result}"

    return decorator


# Second Problem

def even_parameters(decorated_func):
    def decorator(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                return f"Please use only even numbers!"
            else:
                if arg % 2 != 0:
                    return f"Please use only even numbers!"
        return decorated_func(*args, **kwargs)

    return decorator


# Third Problem

def make_bold(decorated_func):
    def decorator(*args, **kwargs):
        result = decorated_func(*args, **kwargs)
        return f"<b>{result}</b>"
    return decorator


def make_italic(decorated_func):
    def decorator(*args, **kwargs):
        result = decorated_func(*args, **kwargs)
        return f"<i>{result}</i>"
    return decorator


def make_underline(decorated_func):
    def decorator(*args, **kwargs):
        result = decorated_func(*args, **kwargs)
        return f"<u>{result}</u>"
    return decorator


# Fourth Problem

def type_check(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, types):
                    return f"Bad Type"
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Fifth Problem
import functools


def cache(func):
    @functools.wraps(func)
    def wrapper(n):
        if not hasattr(wrapper, 'log'):
            wrapper.log = {}
        if n not in wrapper.log:
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Sixth Problem

def tags(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{type}>{result}</{type}>"
        return wrapper
    return decorator


# Seventh Problem

class store_results:
    def __init__(self, func):
        self.func = func
        self.filename = "results.txt"

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        with open(self.filename, "a") as file:
            file.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")
        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)


# Eighth Problem
import time


class exec_time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time


@exec_time
def loop_sum(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop_sum(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop_count():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop_count())
