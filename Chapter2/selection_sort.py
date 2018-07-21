def selectionSort(arr, inplace=False, ascending=True):
    '''输入数组，返回其排序结果
        Parameters
        ---------
          inplace: 就地操作
          ascending: 升序 or 降序

        Return
        ------
          inplace==False时按要求返回排序的数组, 否则返回None
    '''
    def _find_func(arr, index, _min=True):
        from operator import gt, lt

        if _min:
            _op = lt
        else:
            _op = gt
        _idx = index[0]
        _extre = arr[_idx]
        for i in index:
            if _op(arr[i], _extre):
                _idx = i
                _extre = arr[i]
        return _idx

    if inplace:
        tmp = None
        cursor = 0
        while cursor < len(arr) - 1:
            idx2trans = _find_func(arr, list(range(cursor, len(arr))), _min=ascending)
            # 极值和指针指向的位置互换
            arr[cursor], arr[idx2trans] = arr[idx2trans], arr[cursor]
            cursor += 1
    else:
        new = list()
        idx = list(range(len(arr)))
        while len(idx) > 0:
            idx2trans = _find_func(arr, idx, _min=ascending)
            new.append(arr[idx2trans])
            idx.remove(idx2trans)
        return new
