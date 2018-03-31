class Node:
    """Create a Node object"""

    def __init__(self, val, next=None, previous=None):
        """Constructor for the Node object"""
        self.val = val
        self._next = next
        self._previous = previous
        if val is None:
            raise TypeError('Must pass a value')

    def __repr__(self):
        return '{val}'.format(val=self.val)

    def __str__(self):
        return '{val}'.format(val=self.val)
