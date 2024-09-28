from Longest_Palindromic_Substring import longest_palindromic_substring

def test_LongestPalindromicSubstring():

    result = longest_palindromic_substring("babad")
    assert result == "bab" or result == "aba", "Test 1 không đạt"

    assert longest_palindromic_substring("cbbd") == "bb", "Test 2 không đạt"
    assert longest_palindromic_substring("") == "Không được để chuỗi rỗng", "Test 3 không đạt"
    assert longest_palindromic_substring(None) == "Không được để chuỗi rỗng", "Test 4 không đạt"
    assert longest_palindromic_substring("madam") == "madam", "Test 5 không đạt"
    assert longest_palindromic_substring("aaaa") == "aaaa", "Test 6 không đạt"
    assert longest_palindromic_substring("     abbd   ") == "bb", "Test 7 không đạt" 
    assert longest_palindromic_substring("e") == "e", "Test 8 không đạt"
    print("Tất cả test case đều đúng")

test_LongestPalindromicSubstring()
