"""
В исходную строку добавили некоторое количество символов. Необходимо выявить, была ли строка a исходной для строки b.
"""

def is_substr(a, b):
    pa, pb = 0, 0
    while pa<len(a) and pb<len(b):
        if a[pa]==b[pb]:
            pa+=1
            pb+=1
        else:
            pb+=1
    return len(a)==pa