from src.sem3_hash_sort_search.anagrams.anagrams import group_anagrams

def test_empty_list():
    assert group_anagrams([]) == []


def test_single_word():
    result = group_anagrams(["abc"])
    assert result[0] == ["abc"]


def test_all_anagrams():
    result = group_anagrams(["eat", "tea", "ate"])
    assert set(result[0]) == {"eat", "tea", "ate"}


def test_multiple_groups():
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_words)
    expected_groups = [
        {"eat", "tea", "ate"},
        {"tan", "nat"},
        {"bat"}
    ]
    result_groups = [set(group) for group in result]
    for expected in expected_groups:
        assert expected in result_groups
