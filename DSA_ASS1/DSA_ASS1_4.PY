def count_pairs_with_sum(arr: List[int], target_sum: int) -> int:
    freq = {}
    count = 0
    for num in arr:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count
