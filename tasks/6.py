arr = [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]

def binary_array_to_number(arr):
    end = []
    while len(arr) > 0:
        a = len(arr)
        end.append(arr[0] * 2 ** a)
        arr.pop(0)

    print(sum(end))

binary_array_to_number(arr)