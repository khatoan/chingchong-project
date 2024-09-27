def is_palindrome(s: str):
    if s == s[::-1]:
        return True
    else: 
        return False

def longest_palindromic_substring(s: str):
    longest_substring = ""  # Khởi tạo chuỗi palindrome dài nhất
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]  # Lấy chuỗi con từ i đến j
            if is_palindrome(substring) and len(substring) > len(longest_substring) :
                longest_substring = substring

    return    longest_substring 
