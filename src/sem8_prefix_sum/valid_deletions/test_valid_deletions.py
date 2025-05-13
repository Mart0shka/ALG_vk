from valid_deletions import can_make_valid_with_deletions

def test_can_make_valid_with_deletions_case_1():
    s = "()()()"
    k = 4
    assert can_make_valid_with_deletions(s, k) == True

def test_can_make_valid_with_deletions_case_2():
    s = "((("
    k = 1
    assert can_make_valid_with_deletions(s, k) == False

def test_can_make_valid_with_deletions_case_3():
    s = "())"
    k = 1
    assert can_make_valid_with_deletions(s, k) == True

def test_can_make_valid_with_deletions_case_4():
    s = "(()"
    k = 1
    assert can_make_valid_with_deletions(s, k) == True

def test_can_make_valid_with_deletions_case_5():
    s = "(()())"
    k = 0
    assert can_make_valid_with_deletions(s, k) == True

def test_can_make_valid_with_deletions_case_6():
    s = "(())))("
    k = 2
    assert can_make_valid_with_deletions(s, k) == False

def test_can_make_valid_with_deletions_case_7():
    s = "()"
    k = 0
    assert can_make_valid_with_deletions(s, k) == True

def test_can_make_valid_with_deletions_case_8():
    s = "))))))("
    k = 2
    assert can_make_valid_with_deletions(s, k) == False

