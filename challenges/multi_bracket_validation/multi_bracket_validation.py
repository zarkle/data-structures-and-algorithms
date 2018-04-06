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


def multi_bracket_validation(input):
    """Validate for symantically correct multi-brackets in a string"""
    brackets = Stack()
    for i in input:
        if i == '(' or i == '[' or i == '{':
            brackets.push(i)
        elif i == ')' or i == ']' or i == '}':
            if brackets._size == 0:
                return False
            elif i == ')' and brackets.top.val == '(':
                brackets.pop()
            elif i == ']' and brackets.top.val == '[':
                brackets.pop()
            elif i == '}' and brackets.top.val == '{':
                brackets.pop()
            else:
                return False

    if brackets._size != 0:
        return False
    return True
