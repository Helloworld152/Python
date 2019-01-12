def Hanoi(a, b, c, n):
    if n == 0:
        return
    Hanoi(a, c, b, n - 1)
    print("Take the %dth from %c to %c" % (n, a, c))
    Hanoi(b, a, c, n - 1)


Hanoi("A", "B", "C", 8)
