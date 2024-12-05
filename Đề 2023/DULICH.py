file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2023/DULICH.INP", "r")
n = int(file_input.readline())
from collections import Counter
a=[]
for i in range(n):
    k = file_input.readline().split()
    for j in range(len(k)):
        a.append(int(k[j]))
count=Counter(a)
max_count=max(count.values())