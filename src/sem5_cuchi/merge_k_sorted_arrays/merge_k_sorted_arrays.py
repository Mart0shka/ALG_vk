import heapq


def merge_k_sorted_arrays(sorted_arrays):
    merged_array = []

    min_heap = []

    for i in range(len(sorted_arrays)):
        curr_array = sorted_arrays[i]

        if len(curr_array)>0:
            heapq.heappush(min_heap, (curr_array[0], i, 0))

    while len(min_heap)>0:
        value, array_id, elem_id = heapq.heappop(min_heap)
        merged_array.append(value)

        if elem_id + 1 < len(sorted_arrays[array_id]):
            next_elem = sorted_arrays[array_id][elem_id+1]
            heapq.heappush(min_heap, (next_elem, array_id, elem_id+1))

    return merged_array