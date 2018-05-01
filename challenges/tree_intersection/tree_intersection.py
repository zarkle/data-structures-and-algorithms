from .bst import BST


def tree_intersection(bst1, bst2):
    """Return a set of values found in two binary tree parameters."""
    set1 = set()
    set2 = set()

    bst1.pre_order(lambda n: set1.add(n.val))
    bst2.pre_order(lambda n: set2.add(n.val))

    return set1.intersection(set2)
