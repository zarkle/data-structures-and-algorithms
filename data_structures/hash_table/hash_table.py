"""Code hash table."""
# from functools import reduce


class HashTable:
    """Hash table class."""

    def __init__(self, max_size=1024):
        """Init."""
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        """Make a key."""
        if type(key) is not str:
            raise TypeError('Invalid key')

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self, key, val):
        """Set function."""
        # need to handle collisions here
        # values may look something like a DB record:
        # {'id': '123', 'name': 'xxx', 'title': 'zzz',}

        # idx = self.hash_key(key)
        # self.buckets[idx] = val
        self.buckets[self.hash_key(key)] = val

    def get(self, key):
        """Get function."""
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        """Remove function."""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
