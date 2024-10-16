"""
Bạn được cho một xâu word = “a” và một số nguyên k. Khởi đầu, từ xâu word = “a” sẽ phát sinh ra xâu kế tiếp trong bảng chữ cái alphabet là generated = “b” và ghép nối vào word. Như vậy, sau thao tác ban đầu ta được: word = “ab” và generated = “b”. Tiếp tục như vậy, thao tác tiếp theo: generated = “bc” và ghép nối vào word, khi đó word = “abbc”.
Cứ tiếp tục như vậy cho đến khi độ dài của word  >= k thì dừng. Kết quả trả về là kí tự thứ k trong word.
Bạn hãy xây dựng hàm kthCharacter(k) để giải bài toán trên.
•	Lưu ý: Bảng chữ cái sẽ quay vòng, kí tự kế tiếp của “z” là “a”.

Ví dụ:
Input 1: k=5
Output: “b”
Giải thích:
Khởi tạo, word = “a”, ta cần 3 thao tác:
•	Generated = “b”, word = “ab”.
•	Generated = “bc”, word = “abbc”.
•	Generated = “bcd”, word = “abbcbcd”. Lúc này độ dài của word là 7 >=5. Dừng.

Giới hạn:  1 <= k <=500

"""
def kthCharacter(k):
    word = "a"
    generated = "b"

    while len(word) < k:
        word += generated

        if generated[-1] == 'z':
            generated += 'a'
        else:
            generated += chr(ord(generated[-1]) + 1)

    return word[k-1]