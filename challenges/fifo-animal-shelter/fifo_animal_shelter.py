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


class AnimalShelter:
    """Create a FIFO AnimalShelter class"""
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        return f'Oldest animal in the shelter is {self.front.val}'

    def enqueue(self, animal=None):
        """Insert an animal to the back of the queue"""
        if animal != 'dog' and animal != 'cat':
            raise ValueError('Animal not allowed')

        node = Node(animal)
        self._size += 1
        if self.front is None:
            self.front = self.back = node
        self.back._next = node
        self.back = node
        return None

    def dequeue(self, pref=None):
        """Remove the next animal in the queue that matches pref if pref is given; otherwise, remove animal at front of queue"""
        if self._size == 0:
            raise IndexError('No animals')

        if pref is None or self.front.val == pref:
            removed_animal = self.front
            self.front = self.front._next
            self._size -= 1
            return removed_animal.val

        if type(pref) is not str:
            raise TypeError('Invalid animal')

        if pref != 'dog' and pref != 'cat':
            raise ValueError('Animal not allowed')

        current = self.front._next
        temp = self.front
        while current:
            if current.val == pref:
                removed_animal = current
                temp._next = current._next
                self._size -= 1
                return removed_animal.val
            current = current._next
            temp = temp._next
