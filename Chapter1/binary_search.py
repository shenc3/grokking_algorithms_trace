def binarySearch(sorted_list, num):
    '''input a sorted list, if num in it, return the corresponding index'''
    start = 0
    end = len(sorted_list) - 1
    while start < end - 1:
        mid = start + (end - start) // 2
        if num < sorted_list[mid]:
            end = mid
        elif num > sorted_list[mid]:
            start = mid + 1
        else:
            result = mid
            break
    if sorted_list[start] == num:
        result = start
    elif sorted_list[end] == num:
        result = end
    else:
        result = None
    return result
