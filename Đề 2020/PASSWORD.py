'''
Bài 1 (6 điểm): Mật khẩu
Sau một thời gian không sử dụng E-mail, Minh quên mất mật khẩu đăng nhập. Minh chỉ nhớ rằng mật khẩu là một số nguyên lớn nhất có N chữ số và tổng các chữ số của nó đúng bằng S.
Yêu cầu: Bạn hãy giúp Minh tìm lại mật khẩu.
Dữ liệu vào: Từ tệp văn bản PASSWORD.INP ghi hai số nguyên dương N và S (1 ≤ N ≤ 10**4, 0 ≤ S  ≤ 10**6) trên cùng dòng và được ghi cách nhau một dấu cách.
Kết quả: Ghi ra tệp văn bản PASSWORD.OUT một số nguyên duy nhất là mật khẩu cần  tìm. Nếu không tìm được thì ghi số -1
'''

file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/PASSWORD.INP", "r")
s1 = file_input.readline()
A = [int(i) for i in s1.split()]
N = A[0]
S = A[1]

def find_password(N, S):
    if S > 9 * N or (S == 0 and N > 1):
        return -1
        
    result = [0] * N
    tong_con_lai = S
    
    for i in range(N):
        chu_so_lon_nhat = min(9, tong_con_lai)
        result[i] = chu_so_lon_nhat
        tong_con_lai -= chu_so_lon_nhat

    password = int("".join(str(i) for i in result))
    return password

file_output = open("C:/Users/komodo/Documents/chingchong-project/Đề 2020/PASSWORD.OUT", "w")
print(find_password(N,S), file=file_output)