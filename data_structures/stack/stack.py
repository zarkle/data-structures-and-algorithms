from .node import Node


class Stack:
    """Create a Stack data structure"""
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.insert(item)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass
