"""Fizz buzz on BST."""


def fizzbuzztree(tree):
    """Conduct “FizzBuzz” on a tree while traversing through it. Uses in_order traversal."""
    tree.in_order(replace)
    return tree


def replace(node):
    """Fizz buzz helper function."""
    if type(node.val) is int:
        if node.val % 15 == 0:
            node.val = 'fizz buzz'
        elif node.val % 3 == 0:
            node.val = 'fizz'
        elif node.val % 5 == 0:
            node.val = 'buzz'
    return
