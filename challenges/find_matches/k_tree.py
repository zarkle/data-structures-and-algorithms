from .queue import Queue


class Node:
    """create a Node for a K-ary tree"""
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return f'Node value is {self.val}'


class KTree:
    """create a K-ary tree data structure"""
    def __init__(self):
        self.root = None

    def __repr__(self):
        return '<Tree Root {}>'.format(self.root.val)

    def __str__(self):
        return f'Tree root value is {self.root.val}'

    def insert(self, val, parent):
        """
        insert node into K-ary tree at the first instance of a given parent value; note: recursion stops after node is inserted
        """
        node = Node(val)
        current = self.root

        if parent is None:
            if self.root is None:
                self.root = node
                return node
            raise ValueError('Parent value not found')

        def _walk(current=None):
            if current.val == parent:
                current.children.append(node)
                return node
            for child in current.children:
                inserted = _walk(child)
                if inserted:
                    return inserted

        node = _walk(self.root)
        if node is None:
            raise ValueError('Parent value not found')
        return node

    def pre_order_traversal(self, operation):
        """pre-order traversal of K-ary tree"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)
