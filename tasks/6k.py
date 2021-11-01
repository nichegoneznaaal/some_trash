arr = [1, 1, 1, 2, 1, 1]


def find_uniq(arr):
    c = 0
    b = len(arr)
    f = arr[b - 1]
    for m in arr:
        if m == f:
            for i in arr:
                for a in arr:
                    if i != a:
                        c = a
        else:
            return(arr[b - 1])
    print(c)
    return

print(find_uniq(arr))