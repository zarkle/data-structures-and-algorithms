from .hash_table import HashTable as HT


def unique_char(string):
    """."""
    individuals = set()
    string = ''.join(string.lower().split(' '))
    for char in string:
        if char in individuals:
            return False
        individuals.add(char)
    return True
