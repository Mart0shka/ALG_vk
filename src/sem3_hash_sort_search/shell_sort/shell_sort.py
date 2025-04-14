def shell_sort(arr):
    n = len(arr)
    gap = len(arr)//2
    while gap>0:
        for current_position in range(gap, n):
            m_gap = current_position
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap-gap] =  arr[m_gap-gap], arr[m_gap]
                m_gap -= gap
        gap = gap//2
    return arr