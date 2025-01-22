"""
Bài 1 (6 điểm): Mật khẩu
Sau một thời gian không sử dụng E-mail, Minh quên mất mật khẩu đăng nhập. Minh chỉ nhớ rằng mật khẩu là một số nguyên lớn nhất có N chữ số và tổng các chữ số của nó đúng bằng S.
Yêu cầu: Bạn hãy giúp Minh tìm lại mật khẩu.
Dữ liệu vào: Từ tệp văn bản PASSWORD.INP ghi hai số nguyên dương N và S (1 ≤ N ≤ 10**4, 0 ≤ S  ≤ 10**6) trên cùng dòng và được ghi cách nhau một dấu cách.
Kết quả: Ghi ra tệp văn bản PASSWORD.OUT một số nguyên duy nhất là mật khẩu cần  tìm. Nếu không tìm được thì ghi số -1
"""

"""
file_input = open(
    "C:/Users/komodo/Documents/chingchong-project/Đề 2020/PASSWORD.INP", "r"
)
s1 = file_input.readline()
A = [int(i) for i in s1.split()]
N = A[0]
S = A[1]
"""


def file_input(file_path):
    try:
        with open(file_path, "r") as file_input:
            s = file_input.readline()
        if not s:
            print("File input is empty")
            return None
        Data = [int(i) for i in s.split()]
        if len(Data) != 2:
            raise ValueError
        return Data
    except FileNotFoundError:
        print("Can't find file input")
        return None
    except ValueError:
        print("File input must contain exactly 2 integersgers")
        return None


def file_output(file_path, result):
    try:
        with open(file_path, "w") as file_output:
            print(result, file=file_output)
    except Exception as e:
        print(f"Lỗi khi ghi vào file đầu ra: {e}")


def find_password(N, S):
    if N == 0 or S > 9 * N or (S == 0 and N > 1):
        return -1

    result = [0] * N
    tong_con_lai = S

    for i in range(N):
        chu_so_lon_nhat = min(9, tong_con_lai)
        result[i] = chu_so_lon_nhat
        tong_con_lai -= chu_so_lon_nhat

    password = int("".join(str(i) for i in result))
    return password


Data = file_input("C:/Users/komodo/Documents/chingchong-project/Đề 2020/PASSWORD.INP")
if Data:
    N, S = Data[0], Data[1]
    result = find_password(N, S)
else:
    result = -1
file_output("C:/Users/komodo/Documents/chingchong-project/Đề 2020/PASSWORD.OUT", result)
