from kthCharacter import kthCharacter
def unitest_kthCharacter():
    assert(kthCharacter(1)) == "a", "Test 1 không đạt"
    assert(kthCharacter(2)) == 'b', "Test 2 không đạt"
    assert(kthCharacter(3)) == "b", "Test 3 không đạt"
    assert(kthCharacter(5)) == "b", "Test 4 không đạt"
    assert(kthCharacter(10)) == "d", "Test 5 không đạt"
    assert(kthCharacter(500)) == "d", "Test 6 không đạt"
    assert(kthCharacter(None)) == None, "Test 7 không đạt"
    assert(kthCharacter("a")) == None, "Test 8 không đạt"
    print("Tất cả test case đều đúng")
unitest_kthCharacter()