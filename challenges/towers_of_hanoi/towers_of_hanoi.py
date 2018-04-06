def towers_of_hanoi(n):
    """
    Towers of Hanoi function setup
    Puts all disks on tower 'a' (which is a list) to begin with, with the smallest disk (1) on top (which is at the end of the list)
    Returns the number of steps needed to complete the game and the values for
    Towers 'c', 'b', and 'a'
    """
    a = []
    b = []
    c = []
    for i in reversed(range(1, n + 1)):
        a.append(i)
    count = recur(n, a, c, b)
    return (count, c, b, a)


def recur(n, a, c, b):
    """recursion helper function"""
    count = 0
    if n >= 1:
        first = recur(n - 1, a, b, c)
        c.append(a.pop())
        count += 1
        second = recur(n - 1, b, c, a)
        count += first + second
    return count
