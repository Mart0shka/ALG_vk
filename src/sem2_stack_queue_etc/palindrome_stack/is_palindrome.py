from collections import deque

"""
Напишите функцию, которая принимает на вход строку и возвращает true, если она является палиндромом*. В противном случае верните false.
"""

def is_palindrome(a):
    stack = deque()
    for s in a:
        stack.append(s)

    for s in a:
        if s != stack.pop():
            return False
    return True