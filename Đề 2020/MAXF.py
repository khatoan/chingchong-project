"""
Bài 3 (5 điểm): Phân số lớn nhất
Cho một dãy gồm N số nguyên không âm A1, A2, …, AN.
Yêu cầu: Hãy chọn một cặp số trong dãy, trong đó một số làm tử số và một số làm mẫu số để tạo thành một phân số mà phân số đó có giá trị lớn nhất nhỏ hơn 1.
Dữ liệu vào: Từ tệp văn bản MAXF.INP gồm:
+ Dòng đầu ghi số nguyên N (2 ≤ N ≤ 105)
+ Dòng thứ hai ghi N số nguyên A1, A2, …, AN (Ai ≤ 10^9, i = 1...N). Giữa các số được ghi cách nhau một dấu cách.
Kết quả: Ghi ra tệp văn bản MAXF.OUT cặp số tìm được theo thứ tự tử số trước, mẫu số sau. Nếu tìm được nhiều kết quả thỏa yêu cầu bài toán thì in cặp số nhỏ nhất.
Nếu không tìm được kết quả theo yêu cầu bài toán thì ghi số -1.

"""


def input_file(file_path):
    try:
        with open(file_path, "r") as file_input:
            Data = file_input.readlines()
        if len(Data) < 2:
            print("Input file must contain at least two lines.")
            return None
        N = int(Data[0])
        if not Data[1].strip():
            print("The second line in the input file is empty")
            return None
        A = [int(i) for i in Data[1].split()]
        if N != len(A):
            raise ValueError
        return A, N
    except FileNotFoundError:
        print("Can't find file input")
        return None
    except ValueError:
        print("In file input, the number of corresponding values must equal N.")
        return None


def output_file(file_path, result):
    try:
        with open(file_path, "w") as file_output:
            if result != -1:
                a, b = result
                print(a, b, file=file_output)
            else:
                c = result
                print(c, file=file_output)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# Brute force
def main_2(N, A):
    A.sort()
    F = 0
    a = b = None
    for i in range(N):
        for j in range(i + 1, N):
            x = A[i] / A[j]
            if x > F and x < 1:
                F = x
                a, b = A[i], A[j]
    if a is None or b is None:
        return -1
    else:
        return a, b


result = input_file("C:/Users/komodo/Documents/chingchong-project/Đề 2020/MAXF.INP")
if result:
    A, N = result
    result = main_2(N, A)
else:
    result = -1
output_file("C:/Users/komodo/Documents/chingchong-project/Đề 2020/MAXF.OUT", result)
