# quick_sort.py
def quick_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers.")
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
