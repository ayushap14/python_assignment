def find_duplicates(arr: List[int]) -> List[int]:
    freq = {}
    duplicates = []
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        if freq[num] > 1:
            duplicates.append(num)
    return duplicates
