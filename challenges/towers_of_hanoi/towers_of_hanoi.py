# class Node:
#     """Create a Node object"""

#     def __init__(self, val, next=None):
#         """Constructor for the Node object"""
#         self.val = val
#         self._next = next
#         if val is None:
#             raise TypeError('Must pass a value')

#     def __repr__(self):
#         return '{val}'.format(val=self.val)


# class Stack:
#     """Create a Stack data structure"""
#     def __init__(self, iterable=[]):
#         self.top = None
#         self._size = 0
#         if type(iterable) is not list:
#             raise TypeError('Invalid iterable')
#         for item in iterable:
#             self.push(item)

#     def __repr__(self):
#         return f'Top of stack is {self.top.val}'

#     def push(self, val):
#         """Insert a node to top of stack"""
#         try:
#             node = Node(val, self.top)
#         except TypeError:
#             return self.top
#         self.top = node
#         self._size += 1
#         return

#     def pop(self):
#         """Remove the top node from stack"""
#         removed_node = self.top
#         self.top = self.top._next
#         self._size -= 1
#         return removed_node


def towers_of_hanoi(n):
    a = b = c = []
    count = 0
    for i in reversed(range(1, n + 1)):
        a.append(i)
    for i in range(1, 2**n):
        count += 1
        if i % 3 == 1:
            c.append(a.pop())
        if i % 3 == 2:
            b.append(a.pop())
        if i % 3 == 0:
            b.append(c.pop())
    if n % 2 == 0:
        return (count, b)
    if n % 2 == 1:
        return (count, c)



# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)

# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)

https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
