class Node:
    """create a Node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):  # pragma: no cover
        return 'Node Val: {}'.format(self.val)

    def __str__(self):  # pragma: no cover
        return self.val


class BST:
    """create a binary search tree data structure"""
    def __init__(self, iterable=[]):
        self.root = None
        if type(iterable) is not list:
            raise TypeError
        for item in iterable:
            self.insert(item)

    def __repr__(self):  # pragma: no cover
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):  # pragma: no cover
        return self.root.val

    def in_order(self, operation):
        """insert in order"""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def insert(self, val):
        """insert node into BST"""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break
            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node


def fizzbuzztree(tree):
    """Conduct “FizzBuzz” on a tree while traversing through it. Uses in_order traversal"""
    tree.in_order(replace)
    return tree


def replace(node):
    """fizz buzz helper function"""
    if type(node.val) is int:
        if node.val % 15 == 0:
            node.val = 'fizz buzz'
        elif node.val % 3 == 0:
            node.val = 'fizz'
        elif node.val % 5 == 0:
            node.val = 'buzz'
    return

