def _merge(a1, a2):
    i1, i2 = 0, 0
    result = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            result.append(a1[i1])
            i1 += 1
        else:
            result.append(a2[i2])
            i2 += 1
    if i1 <= len(a1) - 1:
        result = result + a1[i1:]
    if i2 <= len(a2) - 1:
        result = result + a2[i2:]
    return result

def mergeSort(array, inplace=False, ascending=True):
    '''输入一个数组，返回其排序结果'''

    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        return _merge(mergeSort(array[:mid]), mergeSort(array[mid:]))
