def kth_smallest_largest_sort(arr: List[int], k: int) -> Tuple[int, int]:
    arr_sorted = sorted(arr)
    kth_smallest = arr_sorted[k - 1]
    kth_largest = arr_sorted[-k]
    return kth_smallest, kth_largest
