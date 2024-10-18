# Bạn được cho một  mảng số nguyên. Hãy xây dựng hàm minElement(nums) để thay thế  mỗi chữ số trong mảng với tổng các chữ số của nó. Kết quả trả về là số nhỏ nhất của mảng sau khi đã thay thế.
"""
Ví dụ.
Input 1: nums = [10, 12, 13, 14]
Output 1: 1
Explanation: Sau khi thay thế nums trở thành [1, 3, 4, 5], giá trị min là 1.
Giới hạn:
•	1<=nums.length<=100
•	1<=nums[i]<=10^4
"""
def Tong(s):
    T = 0
    while s > 0:
        T += s%10
        s = s // 10 
    return T
def minElement(nums):
    if nums == None or nums == []: 
        print("Đầu vào không hợp lệ")
        return None
    try:
        A = [ Tong(i) for i in nums]
        return min(A)
    except:
        print("Đầu vào không hợp lệ")
        return None 
