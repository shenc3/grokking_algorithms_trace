def quickSort(array, inplace=False, ascending=True):
    '''输入一个数组，返回其排序结果

    `Todo`:
      实现inplace的版本
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        small = [i for i in array[1:] if i < pivot]
        large = [i for i in array[1:] if i > pivot]
        return quickSort(small) + [pivot,] + quickSort(large)

