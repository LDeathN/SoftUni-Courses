# First Problem

def number_increment(numbers):

    def increase():
        for i in range(len(numbers)):
            numbers[i] += 1
        return numbers

    return increase()


# Second Problem

def vowel_filter(function):
    vowels = "AaEeOoUuIiYy"

    def wrapper():
        result = function()
        filtered = [letter for letter in result if letter in vowels]
        return filtered
    return wrapper


# Third Problem

def even_numbers(function):

    def wrapper(numbers):
        result = function(numbers)
        even = [num for num in result if num % 2 == 0]
        return even
    return wrapper


# Fourth Problem

def multiply(times):
    def decorator(function):
        def wrapper(number):
            result = function(number)
            return result * times
        return wrapper
    return decorator
