class Node:
    """Create a Node object"""

    def __init__(self, val, next=None):
        """Constructor for the Node object"""
        self.val = val
        self._next = next

    def __repr__(self):
        return f'{self.val}'

    def __str__(self):
        return f'{self.val}'
