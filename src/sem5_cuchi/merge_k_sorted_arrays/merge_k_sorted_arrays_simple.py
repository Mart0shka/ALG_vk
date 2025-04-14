import heapq
def merge_k_sorted_arrays_simple(sorted_arrays):
    min_heap = []

    for array in sorted_arrays:
        for elem in array:
            heapq.heappush(min_heap, elem)

    merged_array = []
    while len(min_heap)>0:
        merged_array.append(heapq.heappop(min_heap))

    return merged_array