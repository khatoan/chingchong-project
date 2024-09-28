# Hàm kiểm tra 1 chuỗi có phải là xâu đối xứng
def check_palindromic(s: str): 
    return s == s[::-1]

def longest_palindromic_substring(s: str):
    if s == None or s == "":
        return "Tham số không hợp lệ"
    s = s.strip()
    # Khởi tạo chuỗi palindrome dài nhất
    longest_substring = ""  
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]  # Lấy chuỗi con từ i đến j
            if check_palindromic(substring) and len(substring) > len(longest_substring) :
                longest_substring = substring

    return    longest_substring 
