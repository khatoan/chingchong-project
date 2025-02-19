"""
**Bài 1: Gà vương**
Vua gà tổ chức cuộc thi để chọn những chú gà có khả năng trở thành Gà Vương. Để được chọn, mỗi chú gà phải thỏa mãn các tiêu chí:
1. **Số thứ tự của chú gà phải là số nguyên tố.**
2. **Chú gà phải có khối lượng lớn nhất trong các chú gà có cùng màu.**
3. **Chú gà có màu đúng với màu mà Vua yêu cầu.**

### Dữ liệu vào: Tệp `GAVUONG.INP`
1. **Dòng 1**: Số nguyên N(số lượng gà tham gia, 1<=N<=10^6)
2. **Dòng 2**: Kí tự K (màu sắc yêu cầu)
2. **Dòng 3**: N số nguyên a_1, a_2, a_3,...,a_N là khối lượng tương ứng của từng chú gà(1<=a_i<=10^6).
3. **Dòng 4**: N ký tự viết hoa, mỗi ký tự là màu của một chú gà.

### Dữ liệu ra: Tệp `GAVUONG.OUT`
1. **Dòng 1**: Số lượng chú gà được chọn. Nếu không có, ghi 0.
2. **Dòng 2**: Các số thứ tự của các chú gà được chọn, tăng dần. Nếu không có, ghi 0.
Ex: 
Input:
10
E
11 11 11 3 11 10 11 5 1 6
ABEEEBCCBE
Output:
2
3 5 

"""

import math


def input_file(file_path):
    with open(file_path, "r") as file_input:
        data = file_input.read().splitlines()

    s1, s2, s3, s4 = data[0], data[1], data[2], data[3]
    N = int(s1)
    K = s2
    weight_list = [int(i) for i in s3.split()]
    color_list = [i for i in s4.strip()]
    return N, K, weight_list, color_list


def prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    result_max = max(weight_list)
    result = []
    for i in range(len(weight_list)):
        if prime(i + 1) and color_list[i] == K:
            if weight_list[i] == result_max:
                result.append(i + 1)
    return result


def output_file(file_path, result):
    try:
        with open(file_path, "w") as file_output:
            print(len(result), file=file_output)
            for i in result:
                print(i, end=" ", file=file_output)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


N, K, weight_list, color_list = input_file(
    "C:/Users/komodo/Documents/chingchong-project/Đề 2022/GAVUONG.INP"
)
result = main()
output_file("C:/Users/komodo/Documents/chingchong-project/Đề 2022/GAVUONG.OUT", result)
