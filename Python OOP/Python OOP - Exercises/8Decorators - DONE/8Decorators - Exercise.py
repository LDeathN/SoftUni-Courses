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



