from .linked_list import LinkedList as LL
from .node import Node


def is_palindrome(list1):
    """Is a singly linked list a palindrome"""
    list2 = []
    current = list1.head
    while current is not None:
        list2 = [current.val] + list2
        current = current._next

    current = list1.head
    for i in range(len(list2)):
        if current.val != list2[i]:
            return False
        current = current._next
    return True
