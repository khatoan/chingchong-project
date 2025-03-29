# Return the nth Fibonacci number using iterative
def fiboIter(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
