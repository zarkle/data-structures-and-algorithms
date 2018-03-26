from node import Node


class LinkedList:
    """
    create a linked list
    """

    def __init__(self, iterable=[]):
        """Constructor for the LinkedList object"""
        self._current = None
        self.head = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
                self.insert(item)

    def __repr__(self):
        return f'<head> is {self.head.val}'

    def __str__(self):
        return self.__repr__

    def __len__(self):
        """Return the size of the linked list"""
        return self._size

    def insert(self, val):
        """Add a value to the head of the linked list"""
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        """Find an item in the linked list"""
        self._current = self.head
        while self._current:
            if self._current.val == val:
                return True
            self._current = self._current._next
        else:
            return False
