def rec_zo_seq(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    return rec_zo_seq(n-1) + rec_zo_seq(n-2)