class Node:
    """Create a Node object"""

    def __init__(self, val, next=None):
        """Constructor for the Node object"""
        self.val = val
        self._next = next
        if val is None:
            raise TypeError('Must pass a value')

    def __repr__(self):
        return '{val}'.format(val=self.val)

    def __str__(self):
        return '{val}'.format(val=self.val)


class Stack:
    """Create a Stack data structure"""
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        self.max = None
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
        if type(val) is int:
            self.get_max(val)
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

    def get_max(self, val=None):
        """Determine the maximum value of stack; value must be integer"""
        if val is None:
            return self.max
        elif self.max is None:
            self.max = val
        elif self.max < val:
            self.max = val
        return self.max

