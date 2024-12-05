file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2022/GAVUONG.INP")
import math
s1 = file_input.readline()
s2 = file_input.readline()
s3 = file_input.readline()
s4 = file_input.readline()
N, K = int(s1), s2.strip()
A = [int(i) for i in s3.split()]
B = [i for i in s4]
file_input.close()

def prime(n:int):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def main():
    result_max = max(A)
    result = []
    for i in range(len(A)):
        if prime(i+1) and B[i] == K:
            if A[i] == result_max:
                result.append(i+1)
    return result

file_output = open("C:/Users/komodo/Documents/chingchong-project/Đề 2022/GAVUONG.OUT", "w")
result = main()
print(len(result), file = file_output)
for i in result:
    print(i, end = " ", file = file_output)
file_output.close()