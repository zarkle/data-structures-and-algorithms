from .node import Node


class Stack:
    """Create a Stack data structure"""
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.push(item)

    def __repr__(self):
        return f'Top of stack is {self.top.val}'

    def __str__(self):
        return f'Top of stack is {self.top.val}'

    def __len__(self):
        """Return the size of the stack"""
        return self._size

    def push(self, val):
        """Insert a node to top of stack"""
        try:
            node = Node(val, self.top)
        except TypeError:
            return self.top
        self.top = node
        self._size += 1
        return self.top

    def pop(self):
        """Remove the top node from stack"""
        removed_node = self.top
        self.top = self.top._next
        self._size -= 1
        return removed_node.val

    def peek(self):
        """Take a peek at the top node"""
        return self.top.val

