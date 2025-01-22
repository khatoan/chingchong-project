# Chuyển 1 xâu nhị phân thành xâu nhị phân khác gấp K lần xâu cũ


def input_file(file_path):
    try:
        with open(file_path, "r") as file_input:
            Data = file_input.readlines()
        s_binary = Data[1]
        A = [int(i) for i in Data[0].split()]
        n, K = A[0], A[1]
        return K, s_binary
    except FileNotFoundError:
        print("Can't find file input")
        return None


def output_file(file_path, result):
    try:
        with open(file_path, "w") as file_output:
            print(result, file=file_output)
    except Exception as e:
        print(f"Lỗi khi ghi vào file đầu ra: {e}")


K, s_binary = input_file(
    "C:/Users/komodo/Documents/chingchong-project/Đề 2023/NHIPHAN.INP"
)
x = int(s_binary, 2) * K
result = bin(x)[2:]
output_file("C:/Users/komodo/Documents/chingchong-project/Đề 2023/NHIPHAN.OUT", result)
