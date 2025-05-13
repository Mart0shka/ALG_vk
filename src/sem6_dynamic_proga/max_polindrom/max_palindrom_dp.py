'''
Дана строка s. Необходимо найти максимальную подстроку,
которая является палиндромом
'''


def longest_palindrome_dp(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

            if dp[i][j] and length > max_len:
                start = i
                max_len = length

    return s[start:start + max_len]