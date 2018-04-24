from .queue import Queue


class Node:
    """create a Node for a K-ary tree"""
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def __repr__(self):  # pragma: no cover
        return 'Node Val: {}'.format(self.val)

    def __str__(self):  # pragma: no cover
        return f'Node value is {self.val}'


class KTree:
    """create a K-ary tree data structure"""
    def __init__(self):
        self.root = None

    def __repr__(self):  # pragma: no cover
        return '<Tree Root {}>'.format(self.root.val)

    def __str__(self):  # pragma: no cover
        return f'Tree root value is {self.root.val}'

    def pre_order_traversal(self, operation):
        """pre-order traversal of K-ary tree"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)

    def post_order_traversal(self, operation):
        """post-order traversal of K-ary tree"""
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self):
        """return breadth-first-traversal of a K-ary tree"""
        queue = Queue()
        traverse = []

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            traverse.append(current.val)
            for child in current.children:
                queue.enqueue(child)
        return traverse

    def insert(self, val, parent):
        """insert node into K-ary tree at a given parent value"""
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
