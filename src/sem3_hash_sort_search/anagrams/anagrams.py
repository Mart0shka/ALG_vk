def dict_hash(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def group_anagrams(strs):
    groups = []

    for word in strs:
        current_hash = dict_hash(word)
        found = False

        for group_hash, group_words in groups:
            if group_hash == current_hash:
                group_words.append(word)
                found = True
                break

        if not found:
            groups.append((current_hash, [word]))

    return [words for _, words in groups]
