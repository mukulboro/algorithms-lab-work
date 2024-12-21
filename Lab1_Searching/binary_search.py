import math

def binary_search(array:list, key:int)->int:
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == key:
            return mid
        elif key <= array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1 