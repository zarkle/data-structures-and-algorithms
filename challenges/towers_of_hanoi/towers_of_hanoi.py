def towers_of_hanoi(n):
    a = []
    b = []
    c = []
    for i in reversed(range(1, n + 1)):
        a.append(i)
    count = recur(n, a, c, b)
    return (count, c, b, a)


def recur(n, a, c, b):
    count = 0
    if n >= 1:
        first = recur(n - 1, a, b, c)
        c.append(a.pop())
        count += 1
        second = recur(n - 1, b, c, a)
        count += first + second
    return count
