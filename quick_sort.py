def quick_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers.")
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    print(f"Pivot: {pivot}")
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    print(f"Less: {less}, Greater: {greater}")
    
    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)
    
    print(f"Sorted less: {sorted_less}, Sorted greater: {sorted_greater}")
    
    return sorted_less + [pivot] + sorted_greater

# 実行例
arr = [3, 6, 8, 10, 1, 2, 1]
print("Final sorted array:", quick_sort(arr))