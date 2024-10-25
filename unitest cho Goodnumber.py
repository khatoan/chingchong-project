from Goodnumber import count_goodNumber
def check_goodNumber():
    assert count_goodNumber(1) == 5, "Test case 1 failled"
    assert count_goodNumber(4) == 400, "Test case 2 failled"
    assert count_goodNumber(50) == 564908303, "Test case 3 failled"
    assert count_goodNumber(10**15) == 711414395, "Test case 4 failled"
    assert count_goodNumber(None) == None, "Test case 5 failled"
    assert count_goodNumber(3.14) == None, "Test case 6 failled"
    assert count_goodNumber(-1) == None, "Test case 7 failled"
    print("All test case is correct")
check_goodNumber()