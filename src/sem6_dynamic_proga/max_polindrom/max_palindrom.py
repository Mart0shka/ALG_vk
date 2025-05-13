'''
Дана строка s. Необходимо найти максимальную подстроку,
которая является палиндромом
'''

def longest_palindrome(s):
    if not s:
        return ""

    current_max_left = 0
    current_max_right = 0

    def expand_around_center(l: int, r: int):
        nonlocal current_max_left, current_max_right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l) > (current_max_right - current_max_left):
                current_max_right = r
                current_max_left = l
            l -= 1
            r += 1

    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)

    return s[current_max_left:current_max_right + 1]