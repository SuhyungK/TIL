class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * self.size
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        self.top -= 1

    def is_Empty(self):
        if not self.stack:
            return 1
        return 0

    def is_Full(self):
        if self.top == self.size:
            return 1
        return 0

    def peek(self):
        if self.is_Empty():
            raise Exception('This stack is empty')
        return self.stack[-1]

    def __str__(self):
        return str(self.stack[::1])

    # ERROR
    # raise Exception

s1 = Stack(3)
print(s1)
