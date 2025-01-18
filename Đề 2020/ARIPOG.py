"""
Bài 2 (5 điểm): Cấp số cộng
Cho cấp số cộng (um) có công sai d là số nguyên khác 0. 
Tức là: um = um-1 + d (m thuộc N*, m ≥ 2 , d thuộc Z , d != 0).
Ví dụ: Dãy số 2, 5, 8, 11, … là một cấp số cộng với  d = 3 và u1=2.
Yêu cầu: Cho số nguyên u1 là phần tử đầu tiên của một cấp số cộng, công sai d và một số nguyên x. Hãy cho biết x có thuộc (um) không, nếu có thì x là phần tử thứ mấy?
Dữ liệu vào: Từ tệp văn bản ARIPOG.INP chứa ba số nguyên u1, d và x (|u1| ≤10^9, |x| ≤10^9, |d| ≤10^9, d!=0) được ghi cách nhau bởi một dấu cách.
Kết quả: Ghi ra tệp văn bản ARIPOG.OUT một số nguyên duy nhất là vị trí của x trong (um).  Nếu x không thuộc (um) thì ghi số -1.
Ex:
input: 1 3 9
output: -1
Giải thích: Với u1=1 và  d =3 ta có (um) là 1, 4, 7, 10, … Do đó 9 không thuộc (um).

Ex:
input: 2 -2 -6
output: 5
Giải thích: Với u1=2 và  d =-2 ta có (um) là  2, 0, -2, -4, -6, -8, … Do đó -6 thuộc (um) và ở vị trí thứ 5.
"""


def input_file(file_path):
    try:
        with open(file_path, "r") as file_input:
            s1 = file_input.readline()
        A = [int(i) for i in s1.split()]
        if len(A) != 3:
            raise ValueError
        return A
    except FileNotFoundError:
        print("Can't find file input")
        return None
    except ValueError:
        print("File input must contain exactly 3 integers")
        return None


def write_output(file_path, result):
    try:
        file_output = open(file_path, "w")
        print(result, file=file_output)
        file_output.close()
    except Exception as e:
        print(f"Lỗi khi ghi vào file đầu ra: {e}")


# Math formula
def main(u1, d, x):
    if (x - u1) % d == 0:
        n = (x - u1) // d + 1
        if n > 0:
            return n
    return -1


# Brute force
# The code not work for very large values
def main_2(u1, d, x):
    u = u1
    n = 1
    while (d > 0 and u <= x) or (d < 0 and u >= x):
        if u == x:
            return n
        else:
            u += d
            n += 1
    return -1


A = input_file("C:/Users/komodo/Documents/chingchong-project/Đề 2020/ARIPOG.INP")
if A:
    u1, d, x = A[0], A[1], A[2]
result = main(u1, d, x)
write_output("C:/Users/komodo/Documents/chingchong-project/Đề 2020/ARIPOG.OUT", result)
