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
