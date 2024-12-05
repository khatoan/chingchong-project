file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2023/NHIPHAN.INP")
s1 = file_input.readline()
s2 = file_input.readline()
A = [int(i) for i in s1.split()]
n, K = A[0], A[1]

#Đổi từ chuỗi nhị phân sang hệ thập phân và nhân cho K
x = int(s2, 2)*K 
binary = bin(x)[2:]

file_output = open('C:/Users/komodo/Documents/chingchong-project/Đề 2023/NHIPHAN.OUT', "w")
print(binary, file = file_output)
