from node import Node


class LinkedList:
    """
    create a linked list
    """
    def __init__(self, iterable=[]):
        self._current = None
        self.head = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.insert(item)

    def __repr__(self):
        return

    def __str__(self):
        return self.__repr__

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        self._current = self.head
        for i in range(len(self)):
            if self._current == val:
                return True
            self._current = self._current.next
        else:
            return False
