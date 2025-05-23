"""
Сегодня утром жюри решило добавить в вариант олимпиады еще одну,
Очень Легкую Задачу. Ответственный секретарь Оргкомитета напечатал
ее условие в одном экземпляре, и теперь ему нужно до начала олимпиады
успеть сделать еще N копий. В его распоряжении имеются два ксерокса,
один из которых копирует лист за х секунд, а другой – за y.

(Разрешается использовать как один ксерокс, так и оба одновременно.
Можно копировать не только с оригинала, но и с копии.)
Помогите ему выяснить, какое минимальное время для этого потребуется.
"""

def copy_time(n,x,y):
    l = 0
    r = (n-1)*max(x,y)
    while l+1<r:
        mid = (r+l)//2
        if mid//x + mid//y < n-1:
            l = mid
        else:
            r = mid

    return r + min(x,y)