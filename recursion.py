def length(arr):
    if not arr:
        return 0
    else:
        return 1 + length(arr[1:])
# arr1 = [10, 7, 8, 9, 1, 5] 
# print(length(arr1)) #hasilnya 6


