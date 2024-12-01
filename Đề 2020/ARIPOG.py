file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/ARIPOG.INP", "r")
s1 = file_input.readline()
A = [ int(i) for i in s1.split()]
print(A)
u1, d, x = A[0], A[1], A[2]

#Math formula
def main(u1, d, x):
    if (x - u1)%d ==0:
        n = (x - u1)//d+1
        if n > 0:
            return n
    return -1

#Brute force
def main_2(u1, d, x): 
    u = u1
    n = 1
    while (d > 0 and u<=x) or (d < 0 and u>=x):
        if u == x:
            return n
        else:
            u += d
            n += 1
    return -1       

result = main_2(u1, d, x)
file_output = open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/ARIPOG.OUT", "w")
print(result, file = file_output)