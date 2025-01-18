from ARIPOG import main_2
from ARIPOG import main
def test_functions():
    assert main(1, 2, 5) == 3  
    assert main(1, 2, 6) == -1  
    assert main(1,3,9) == -1
    assert main(2,-2,-6) == 5
    assert main(1, 1, 1000000000) == 1000000000
    assert main(2, 5, 1000000000) == -1
    assert main_2(1, 2, 5) == 3
    assert main_2(1, -2, -5) == 4
    print("All test cases passed")
test_functions()