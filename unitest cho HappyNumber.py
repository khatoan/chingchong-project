from Happynumber import HappyNumber
def test_happynumber():
    assert HappyNumber(19) == True, "Test 1 không đạt"
    assert HappyNumber(2) == False, "Test 2 không đạt"
    assert HappyNumber(None) == False, "Test 3 không đạt"
    assert HappyNumber(1) == True, "Test 4 không đạt"
    assert HappyNumber(7) == True, "Test 5 không đạt"
    assert HappyNumber(4) == False, "Test 6 không đạt"
    assert HappyNumber(2147483646) == False, "Test 7 không đạt"
    assert HappyNumber(89) == False, "Test 8 không đạt"
    assert HappyNumber(58) == False, "Test 9 không đạt"
    assert HappyNumber(2**31-1) == False, "Test 10 không đạt"
    print("Tất cả test case đều đạt")
test_happynumber()