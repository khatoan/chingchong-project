def dem(s):
    if s is None or s == "":
        return 0
    x = 0
    for i in s:
        x += 1
    return x
def chingchong(haystack, needle):
    if haystack == "" and needle == "":
        return -1
    if haystack is None or needle is None:
        return -1
    haystack = haystack.strip()
    needle = needle.strip()
    len_haystack = dem(haystack)
    len_needle = dem(needle)
    for i in range(len_haystack):
        if haystack[i:i + len_needle] == needle:
            return i
    else: 
        return -1