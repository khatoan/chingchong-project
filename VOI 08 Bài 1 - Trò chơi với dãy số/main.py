# Đề bài: https://oj.vnoi.info/problem/nksgame
file_input = open("C:/Users/komodo/Documents/chingchong-project/VOI 08 Bài 1 - Trò chơi với dãy số/trochoidayso.inp", 'r')
s1 = file_input.readline()
s2 = file_input.readline()
s3 = file_input.readline()
file_input.close()

n = int(s1)
A = sorted([int(i) for i in s2.split()])
B = sorted([int(i) for i in s3.split()])

def main(A, B):
    Sum_min = float("inf")
    i, j = 0, len(B) - 1
    
    while i < len(A) and j >= 0:
        Sum = A[i] + B[j]
        Sum_min = min(Sum_min, abs(Sum))
        
        if Sum < 0:
            i += 1
        elif Sum > 0:
            j -= 1
        else:
            return 0
    
    return Sum_min

file_out = open("C:/Users/komodo/Documents/chingchong-project/VOI 08 Bài 1 - Trò chơi với dãy số/trochoidayso.out", 'w')
print(main(A,B), file=file_out)
file_out.close()