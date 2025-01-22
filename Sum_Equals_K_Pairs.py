#Đề: https://lqdoj.edu.vn/problem/cntpair02
s1 = input()
s2 = input()
A = s1.split()
n,k = int(A[0]), int(A[1])
B = [int(i) for i in s2.split()]

def main(B: list, k: int) -> int:
    left = 0
    right = len(B) - 1
    count = 0
    while left < right:
        for i in range(left, right):
            if B[i] + B[right] == k:
                count += 1
        right -= 1
    return count

print(main(B,k))