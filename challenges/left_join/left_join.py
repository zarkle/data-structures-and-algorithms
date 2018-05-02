"""Implement a simplified LEFT JOIN for 2 Hashmaps."""


def left_join(hash1, hash2):
    """Left join 2 hash tables."""
    result = []
    for each in hash1.buckets:
        if each:
            for node in each.display():
                result.append(list(node.keys())[0])
                result[-1] = [result[-1], hash1.get(result[-1]), hash2.get(result[-1])]
    return result
