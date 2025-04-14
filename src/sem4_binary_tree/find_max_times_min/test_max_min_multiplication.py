from src.sem4_binary_tree.find_max_times_min.max_min_multiplication import max_min_multiplication
def test_full_bst():
    #        4
    #       / \
    #      2   6
    #     / \ / \
    #    1  3 5 7
    # BFS: [4, 2, 6, 1, 3, 5, 7]
    assert max_min_multiplication([4, 2, 6, 1, 3, 5, 7]) == 7  # 1 * 7


def test_duplicate_values():
    #        3
    #       / \
    #      3   3
    # BFS: [3, 3, 3]
    assert max_min_multiplication([3, 3, 3]) == 9  # 3 * 3

def test_min_max_in_middle():
    #        10
    #       /  \
    #      5    15
    #     /  \
    #    1   6
    # BFS: [10, 5, 15, 1, 6]
    assert max_min_multiplication([10, 5, 15, 1, 6]) == 15  # 1 * 20
