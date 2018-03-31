from linked_list import LinkedList as LL
from node import Node


def reverse_ll(list1):
    """Reverse a singly linked list"""
    current = list1.head
    list2 = LL()
    while current is not None:
        # list2.insert(current)
        list2.head = Node(current, list2.head)
        current = current._next
    return list2.head.val
