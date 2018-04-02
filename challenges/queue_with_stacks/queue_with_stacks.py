from .stack import Stack


class Queue:
    """Create a Queue class that has access to 2 Stack instances with push and pop methods"""
    def __init__(self, iterable=[]):
        self._size = 0
        self.stack_one = Stack()
        self.stack_two = Stack()

        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def enqueue(self, val):
        """"""
        try:
            self.stack_one.push(val)
        except TypeError:
            return self.stack_one.top
        self._size += 1
        return self
