from Elimination_game import lastRemaining
def check_lastRemaining():
    assert lastRemaining(9) == 6, "Test case 1 failled"
    assert lastRemaining(1) == 1, "Test case 2 failled"
    assert lastRemaining(6) == 4, "Test case 3 failled"
    assert lastRemaining(10**9) == 534765398, "Test case 4 failled"
    assert lastRemaining(None) == None, "Test case 5 failled"
    assert lastRemaining(3.14) == None, "Test case 6 failled"
    assert lastRemaining(-1) == None, "Test case 7 failled"
    print("All test case is correct")
check_lastRemaining()