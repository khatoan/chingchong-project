file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/MAXF.INP", "r")
s1 = file_input.readline()
s2 = file_input.readline()
A = [int(i) for i in s2.split()]

# Brute force
def main_2(A):
    A.sort()
    F = 0
    a = b = None
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            x = A[i] / A[j]
            if x > F and x < 1:
                F = x
                a,b = A[i], A[j]
    if a is not None and b is not None:
        return a,b
    else:
        return -1

file_output = (open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/MAXF.OUT", "w"))
result = main_2(A)

if result != -1:
    a,b = result
    print(a,b, file=file_output)
else:
    c = result
    print(c, file = file_output)


file_input.close()
file_output.close()