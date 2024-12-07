'''
Bài 3 (5 điểm): Phân số lớn nhất
Cho một dãy gồm N số nguyên không âm A1, A2, …, AN.
Yêu cầu: Hãy chọn một cặp số trong dãy, trong đó một số làm tử số và một số làm mẫu số để tạo thành một phân số mà phân số đó có giá trị lớn nhất nhỏ hơn 1.
Dữ liệu vào: Từ tệp văn bản MAXF.INP gồm:
+ Dòng đầu ghi số nguyên N (2 ≤ N ≤ 105)
+ Dòng thứ hai ghi N số nguyên A1, A2, …, AN (Ai ≤ 10^9, i = 1...N). Giữa các số được ghi cách nhau một dấu cách.
Kết quả: Ghi ra tệp văn bản MAXF.OUT cặp số tìm được theo thứ tự tử số trước, mẫu số sau. Nếu tìm được nhiều kết quả thỏa yêu cầu bài toán thì in cặp số nhỏ nhất.
Nếu không tìm được kết quả theo yêu cầu bài toán thì ghi số -1.

'''
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