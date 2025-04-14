"""
На вход функции подается две строки: a и b.
Строка b образована из строки a путем перемешивания и
добавления одной буквы.
Необходимо вернуть эту букву
"""

def str_diff(a, b):
    if len(a) < len(b):
        a,b = b,a

    temp_dict = dict()
    for char in a:
        if char in temp_dict:
            temp_dict[char] += 1
        else:
            temp_dict[char] = 1

    for char in b:
        if temp_dict[char] == 1:
            del temp_dict[char]
        else:
            temp_dict[char] -= 1

    return list(temp_dict.keys())[0]
