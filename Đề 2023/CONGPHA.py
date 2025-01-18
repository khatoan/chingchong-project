"""
Bài 1 (6,0 điểm): Công phá  
Hành tinh Alpha đang bị chiếm đóng bởi hành tinh Beta. Quân giải phóng của Alpha đang lên kế hoạch tấn công để giải phóng các thành phố đang bị chiếm đóng của hành tinh này. Đây là cơ hội duy nhất để họ có thể giành chiến thắng. 
Vì vậy họ quyết định sử dụng hết tất cả thuốc nổ trữ trong kho. Hiện tại, họ có n khối thuốc nổ được đánh số từ 1 tới n, khối thứ i có trọng lượng là a_i. Mỗi khối đã được sản xuất và đóng gói riêng, không thể tách thành một khối để sử dụng hay cắt nhỏ trong quá trình thực hiện.

Một khối thuốc nổ có trọng lượng x sẽ có sức công phá bằng tích của x với số lượng ước dương của x. Khối thuốc nổ có trọng lượng là 4 thì sức công phá là 4 X 3 = 12 (4 có 3 ước dương là 1, 2, và 4).

Yêu cầu:  
Hãy tính sức công phá khi quân giải phóng Alpha cho nổ cùng lúc n khối thuốc nổ. Biết rằng, khối nổ cùng lúc khi tổng sức công phá bằng tổng sức công phá của mỗi khối.

**Dữ liệu vào:**  
Từ tệp văn bản `CONGPHA.INP` gồm:  

- Dòng đầu chứa số nguyên dương n (1 <= n <= 10^4) là số lượng các khối thuốc nổ.  
- Dòng thứ hai chứa n số nguyên dương  a_1, a_2,... với a_i là trọng lượng khối thuốc nổ thứ i (1 <= i <=n; 1<=a_i<=10^6).

**Kết quả:**  
Ghi ra tệp văn bản `CONGPHA.OUT` một số nguyên duy nhất là kết quả bài toán.

"""


def input_file(file_path):
    try:
        with open(file_path, "r") as file_input:
            Data = file_input.readlines()
            if not Data:
                print("File input is empty")
                return None
            if len(Data) != 2:
                raise ValueError
            n = int(Data[0])
            A = [int(i) for i in Data[1].split()]
            if len(A) != n:
                print("Number of elements in line 2 must be equal to n")
                return None
            return n, A
    except FileNotFoundError:
        print("Can't find file input")
        return None
    except ValueError:
        print("File input must contain exactly 2 lines")
        return None


def number_of_factors(n: int):
    T = 1
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            T += 1
    return T


def main(A: list):
    x = 0
    for i in A:
        x += i * number_of_factors(i)
    return x


def output_file(file_path, result):
    try:
        with open(file_path, "w") as file_input:
            print(result, file=file_input)
    except Exception as e:
        print(f"Lỗi khi ghi vào file đầu ra: {e}")


Data = input_file("C:/Users/komodo/Documents/chingchong-project/Đề 2023/CONGPHA.INP")
if Data:
    n, A = Data
    result = main(A)
    output_file(
        "C:/Users/komodo/Documents/chingchong-project/Đề 2023/CONGPHA.OUT", result
    )
