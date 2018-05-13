"""Implement a simplified LEFT JOIN for 2 Hash tables."""
from .linked_list import LinkedList as LL


class HashTable:  # pragma: no cover
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
        return 'NULL'


def left_join(hash1, hash2):
    """Left join 2 hash tables."""
    result = []
    for each in hash1.buckets:
        if each:
            for node in each.display():
                result.append(list(node.keys())[0])
                result[-1] = [result[-1], hash1.get(result[-1]), hash2.get(result[-1])]
    return result
