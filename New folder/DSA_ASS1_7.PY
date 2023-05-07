def move_negatives_to_one_side(arr: List[int]) -> List[int]:
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] < 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
    return arr
