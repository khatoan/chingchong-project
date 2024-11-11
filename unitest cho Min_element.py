from Min_element import minElement
from Min_element import Tong
import random
import time

def test_minElement():
    start_time = time.time()

    assert minElement([10,12,13,14]) == 1, "Test 1 không đạt"
    assert minElement([1,2,3,4]) == 1, "Test 2 không đạt"
    assert minElement([99, 19, 199]) == 10, "Test 3 không đạt"
    assert minElement([5]) == 5, "Test 4 không đạt"
    assert minElement([11,20,101,1100]) == 2, "Test 5 không đạt"
    assert minElement([1,10000]) == 1, "Test 6 không đạt"

    nums =  [i for i in range(1, 101)]
    assert minElement(nums) == 1, "Test 7 is incorrect"

    nums1 = [random.randint(1, 1000) for _ in range(100)]
    assert minElement(nums1) == min([Tong(i) for i in nums1]), "Test 8 is incorrect"
    
    assert minElement(["a", 'b', 'c']) == None, "Test 9 is incorrect"
    assert minElement([]) == None, "Test 10 is incorrect"
    assert minElement(None) == None, "Test 11 is incorrect"

    end_time = time.time()

    print("All test case is corect")
    print(f"Thời gian thực thi bộ unittest: {end_time - start_time:.6f} giây")
    
test_minElement()