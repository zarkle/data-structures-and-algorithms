"""Implement a simplified LEFT JOIN for 2 Hashmaps."""


def left_join(hash1, hash2):
    """Left join 2 hash tables."""
    result = []
    for each in hash1:
        if each:
            for node in each.all():
                result.append(node)
    return result
