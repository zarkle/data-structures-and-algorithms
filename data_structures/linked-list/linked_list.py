from node import Node


class LinkedList:
    """
    create a linked list
    """

    def __init__(self, iterable=[]):
        """Constructor for the LinkedList object"""
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
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current._next

        return False

    def append(self, val):
        """Append an item to the end of the linked list"""
        if self.head is None:
            self.insert(val)
        else:
            current = self.head
            while current:
                if current._next is None:
                    current._next = Node(val)
                    self._size += 1
                    break
                current = current._next

    def insert_before(self, val, newVal):
        """
        Add a new node with the given newValue immediately before the first value node
        """
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if previous is None:
                    self.insert(newVal)
                else:
                    new_node = Node(newVal)
                    new_node._next = current
                    previous._next = new_node
                    self._size += 1
                break
            previous = current
            current = current._next

    def insert_after(self, val, newVal):
        """
        Add a new node with the given newValue immediately after the first value node
        """
        current = self.head
        while current:
            if current.val == val:
                position = current._next
                current._next = Node(newVal)
                current._next._next = position
                self._size += 1
                break
            current = current._next

    def kth_from_end(self, k):
        """Return the node that is k from the end of the linked list."""
        if len(self) - k < 0:
            raise AttributeError
        current = self.head
        for i in range(len(self) - k - 1):
            current = current._next
        return current.val


        # current = self.head
        # counter = self._size - 1 - k
        # if (counter < 0) | (counter >= self._size):
        #     raise ValueError
        # while counter > 0:
        #     current = current._next
        #     counter -= 1
        # return current.val
