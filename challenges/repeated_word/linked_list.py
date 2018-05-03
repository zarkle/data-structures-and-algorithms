"""LinkedList."""


class Node:
    """Create a Node object."""

    def __init__(self, val, next=None):
        """Construct the Node object."""
        self.val = val
        self._next = next
        if val is None:
            raise TypeError('Must pass a value')

    def __repr__(self):
        """Repr."""
        return '{val}'.format(val=self.val)

    def __str__(self):
        """String."""
        return '{val}'.format(val=self.val)


class LinkedList:
    """Create a linked list."""

    def __init__(self, iterable=[]):
        """Construct the LinkedList object."""
        self.head = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
                self.insert(item)

    def __repr__(self):
        """Repr."""
        return f'<head> is {self.head.val}'

    def __str__(self):
        """String."""
        return f'<head> is {self.head.val}'

    def __len__(self):
        """Return the size of the linked list."""
        return self._size

    def insert(self, val):
        """Add a value to the head of the linked list."""
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        """Find the node that has the given value."""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current._next

    def append(self, val):
        """Append an item to the end of the linked list."""
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
        """Add a new node with the given newValue immediately before the first value node."""
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
        """Add a new node with the given newValue immediately after the first value node."""
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

    def has_loop(self):
        """Return a boolean that indicates whether or not a circular reference or loop is present in the linked list."""
        a = b = self.head
        while a and b and b._next:
            a = a._next
            b = b._next._next
            if a is b:
                return True
        return False

    def pop(self):
        """Remove and return the value of the head of the linked list."""
        if not self.head:
            raise IndexError('The list is empty')
        output = self.head.val
        self.head = self.head._next
        self._size -= 1
        return output

    def remove(self, node):
        """Remove the given node from the linked list."""
        if self.head is node:
            self.head = self.head._next
            self._size -= 1
            return

        current = self.head
        while current:
            if current._next is node:
                current._next = node._next
                self._size -= 1
                return
            current = current._next

        raise ValueError('Node is not in list.')

    def display(self):
        """Display linked list as if it were an array."""
        current = self.head
        output = []
        while current:
            output.append(current.val)
            current = current._next
        return output
