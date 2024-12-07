'''
Bài 2: Du lịch
1. Nhiệm vụ: Tìm thời điểm có nhiều loài hoa nở rộ nhất dựa trên danh sách các khoảng thời gian nở của từng loài hoa.
2. Dữ liệu đầu vào (*DULICH.INP*):
   - Dòng 1: Chứa số nguyên dương n tương ứng với n loài hoa(1<=n<=10^5).
   - n dòng tiếp theo: Mỗi dòng chứa hai số nguyên a_i và b_i (1<=i<=n; 1<=a_i<=b_i<=10^9) đại diện cho khoảng thời gian loài hoa i nở.
3. Yêu cầu đầu ra (*DULICH.OUT*): 
   - Ghi ra thời điểm có nhiều loài hoa nở rộ nhất.
4. Ex:
    Input:
     6
     1 2
     2 3
     2 5
     5 7
     5 7
     9 11 
    Output:
     2
    **Giải thích**: Thời điểm 2 có 3 loài hoa nở rộ (loài hoa số 1, 2, và 3).
'''
file_input = open("C:/Users/komodo/Documents/chingchong-project/Đề 2023/DULICH.INP", "r")
n = int(file_input.readline())
from collections import Counter
a=[]
for i in range(n):
    k = file_input.readline().split()
    for j in range(len(k)):
        a.append(int(k[j]))
count=Counter(a)
max_count=max(count.values())