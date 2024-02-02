# First Problem

class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1


# Second Problem

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            return self.iterable.pop()
        else:
            raise StopIteration


# Third Problem

class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = "aeiouyAEIOUY"
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            letter = self.text[self.index]
            self.index += 1
            if letter in self.vowels:
                return letter
        raise StopIteration


# Fourth Problem

def squares(number):
    for i in range(1, number + 1):
        yield i ** 2


# Fifth Problem

def genrange(start: int, end: int):
    for i in range(start, end + 1):
        yield i


# Sixth Problem

def reverse_text(text: str):
    for i in reversed(text):
        yield i

