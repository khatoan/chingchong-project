from Min_element import minElement
def test_minElement():
    assert minElement([10,12,13,14]) == 1, "Test 1 không đạt"
    assert minElement([1,2,3,4]) == 1, "Test 2 không đạt"
    assert minElement([99, 19, 199]) == 10, "Test 3 không đạt"
    assert minElement([5]) == 5, "Test 4 không đạt"
    assert minElement([11,20,101,1100]) == 2, "Test 5 không đạt"
    assert minElement([1,10000]) == 1, "Test 6 không đạt"
    print("Tất cả test case đều đạt")
test_minElement()