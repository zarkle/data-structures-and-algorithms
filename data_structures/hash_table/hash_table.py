"""Code hash table."""
from functools import reduce


class HashTable:
    """Hash table class."""

    def __init__(self, max_size=1024):
        """Init."""
        self.max_size = max_size
        self.buckets = [LL()] * self.max_size

    def _hash_key(self, key):
        """Make a hashkey."""
        return reduce(lambda a, b: a + ord(b), list(key), 0) % len(self.buckets)

    def set(self, key, val):
        """Set function."""
        if self.get(key) is None:
            return self.buckets[self._hash_key(key)].append({key: val})
        self.buckets[self._hash_key(key)].append({key: val})

    def get(self, key):
        """Get function."""
        current = LL.head
        while current:
            if key in current.val:
                return current.val[key]
            current = current._next

    def remove(self, key):
        """Remove function."""
        current = LL.head
        while current:
            if key in current._next.val:
                current._next = current.val[key]._next
                return
            current = current._next
