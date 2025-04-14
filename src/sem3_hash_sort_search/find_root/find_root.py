'''
Найти корень числа (ближайшее целое, как я понял, слева)
'''

def find_root(target):
    l, r = 0, target
    while l<=r:
        middle = l + (r-l)//2
        if middle**2 > target:
            r = middle-1
            continue
        if middle**2 < target:
            l = middle+1
            continue
        return middle
    return r
