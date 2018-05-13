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


def repeated_word(long_string):
    """Imperative function that accepts a lengthy string parameter (which contains no punctation) and return the first word to occur sequentially more than once in that provided string."""
    if type(long_string) is not str:
        raise TypeError('Input must be string.')

    individuals = HashTable()
    words = long_string.lower().split(' ')
    for word in words:
        if individuals.get(word) is None:
            individuals.set(word, word)
        else:
            return word
