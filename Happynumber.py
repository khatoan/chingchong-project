def sumSquare(x):
    T = 0
    for i in str(x):
        T += int(i) ** 2
    return T


def HappyNumber(n):
    if n is None:
        return False
    H = set()
    while n != 1:
        n = sumSquare(n)
        if n in H:
            return False
        H.add(n)
    return True


def main():
    nums = 0
    n = int(input("Enter a number: "))
    A = list(map(int, input().split()))
    for i in A:
        if HappyNumber(i):
            nums += 1
    print(nums)


main()
