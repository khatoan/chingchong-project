from Longest_Palindromic_Substring import longest_palindromic_substring

def test_LongestPalindromicSubstring():

    result = longest_palindromic_substring("babad")
    assert result == "bab" or result == "aba", "Test 1 không đạt"

    assert longest_palindromic_substring("cbbd") == "bb", "Test 2 không đạt"

    print("Tất cả test case đều đúng")

test_LongestPalindromicSubstring()
