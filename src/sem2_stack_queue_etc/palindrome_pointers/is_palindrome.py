
"""
Напишите функцию, которая принимает на вход строку и возвращает true, если она является палиндромом*. В противном случае верните false.
"""

def is_palindrome(a):
    for i in range(len(a)//2):
        if a[i]!=a[-i-1]:
            return False
    return True