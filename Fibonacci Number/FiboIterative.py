# Return the nth Fibonacci number using iterative
def fiboIter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
