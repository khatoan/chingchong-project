# unitest cho bài Find the index of the first Occurrence in a String
from Find_the_index_of_the_First_Occurrence_in_a_String import chingchong 
def test_chingchong():
    assert chingchong("sadbutsad", "sad") == 0, "Test 1 không đạt"
    assert chingchong("sadbutsad", "happy") == -1, "Test 2 không đạt"
    assert chingchong("sadbutsad", "") == 0, "Test 3 không đạt"
    assert chingchong("", "sad") == -1, "Test 4 không đạt"
    assert chingchong("sad", "sad") == 0, "Test 5 không đạt"   
    assert chingchong("sadbutsad", "b") == 3, "Test 6 không đạt"
    assert chingchong("", "") == -1, "Test 7 không đạt"
    assert chingchong(None, None) == -1, "Test 8 không đạt" 
    assert chingchong("", None) == -1, "Test 9 không đạt"
    assert chingchong(None, "") == -1, "Test 10 không đạt"
    assert chingchong("      ktoan    ", "toan") == 1, "Test 11 không đạt"
    assert chingchong("   sadbutsad   ", "sad") == 0, "Test 12 không đạt"
    print("Tất cả test case đều đúng")
test_chingchong()