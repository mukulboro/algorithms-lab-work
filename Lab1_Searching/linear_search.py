def linear_search(array:list, key:int)->int:
    for i, item in enumerate(array):
        if item == key: return i
    return -1