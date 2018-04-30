"""Code hash table."""
# from functools import reduce
from .linked_list import LinkedList as LL


class HashTable:
    """Hash table class."""

    def __init__(self, max_size=1024):
        """Init."""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]
        if type(max_size) is not int:
            raise TypeError('Max size must be Integer')

        if max_size < 1:
            raise ValueError('Max size must be non-negative Integer')

    def _hash_key(self, key):
        """Make a hashkey."""
        if type(key) is not str:
            raise TypeError('Key must be String')

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self, key, val):
        """Set function."""
        self.buckets[self._hash_key(key)].append({key: val})

    def get(self, key):
        """Get function."""
        current = self.buckets[self._hash_key(key)].head
        while current:
            if key in current.val.keys():
                return current.val[key]
            current = current._next

    def remove(self, key):
        """Remove function."""
        ll = self.buckets[self._hash_key(key)]
        if key in ll.head.val.keys():
            ll.head = ll.head._next
            return

        current = ll.head
        while current:
            if key in current._next.val.keys():
                current._next = current.val[key]._next
                return
            current = current._next
