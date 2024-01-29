class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def __str__(self):
        return f"[{', '.join(str(element) for element in reversed(self.data))}]"
