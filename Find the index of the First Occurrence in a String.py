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