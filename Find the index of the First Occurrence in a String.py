haystack = "sadbutsad"
needle = "sad"
def dem(s):
    x = 0
    for i in s:
        x += 1
    return x
def chingchong(haystack, needle):
    len_haystack = dem(haystack)
    len_needle = dem(needle)
    for i in range(len_haystack):
        if haystack[i:i + len_needle] == needle:
            return i
    else: 
        return -1
print(chingchong(haystack, needle))

def test_chingchong():
    assert chingchong("sadbutsad", "sad") == 0, "Test 1 không đạt"
    assert chingchong("sadbutsad", "happy") == -1, "Test 2 không đạt"
    assert chingchong("sadbutsad", "") == 0, "Test 3 không đạt"
    assert chingchong("", "sad") == -1, "Test 4 không đạt"
    assert chingchong("sad", "sad") == 0, "Test 5 không đạt"   
    assert chingchong("sadbutsad", "b") == 3, "Test 6 không đạt"
    print("Tất cả test case đều đúng")
test_chingchong()
