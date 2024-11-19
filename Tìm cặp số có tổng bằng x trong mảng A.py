#Đề: https://lqdoj.edu.vn/problem/findpair
#Dùng thuật toán 2 con trỏ
x = input().split()
y = input()
N = int(x[0])
X = int(x[1])
A = [int(i) for i in y.split()]

def main(X,A):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == X:
            return i + 1, j + 1 
        if A[i] + A[j] > X:
            j -= 1
        if A[i] + A[j] < X:
            i += 1
    return None

result = main(X,A)
if result is None:
    print("No solution")
else:
    a,b = result
    print(a,b)