# def towers_of_hanoi(n):
#     a = b = c = []
#     count = 0
#     for i in reversed(range(1, n + 1)):
#         a.append(i)
#     for i in range(1, 2**n):
#         count += 1
#         if i % 3 == 1:
#             c.append(a.pop())
#         if i % 3 == 2:
#             b.append(a.pop())
#         if i % 3 == 0:
#             b.append(c.pop())
#     if n % 2 == 0:
#         return (count, b)
#     if n % 2 == 1:
#         return (count, c)



# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)

# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)


# def towers_of_hanoi(n):
#     a = []
#     b = []
#     c = []
#     for i in reversed(range(1, n + 1)):
#         a.append(i)
#     count = recur(n, a, b, c)
#     return (count, c)


# def recur(n, a, b, c):
#     count = 0
#     if n >= 1:
#         first = recur(n - 1, a, c, b)
#         print('moving disk {} from a to c'.format(a[-1]))
#         c.append(a.pop())

#         count += 1
#         second = recur(n - 1, c, b, a)
#         count += first + second
#     return count
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
# http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
# https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html



def towers_of_hanoi(n):
    a = []
    b = []
    c = []
    for i in reversed(range(1, n + 1)):
        a.append(i)
    count = recur(n, a, c, b)
    return (count, c)


def recur(n, a, c, b):
    count = 0
    if n >= 1:
        first = recur(n - 1, a, b, c)
        c.append(a.pop())
        count += 1
        second = recur(n - 1, b, c, a)
        count += first + second
    return count
