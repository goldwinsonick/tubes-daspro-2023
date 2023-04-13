# a = [1, 2, 3, 4, 5]
# tail = a[1:]
# print(tail)  # Output: [2, 3, 4, 5]

def length(arr):
    if not arr:
        return 0
    else:
        return 1 + length(arr[1:])
# arr1 = [10, 7, 8, 9, 1, 5]
# print(length(arr1)) #hasilnya 6


def splits(arr, splitter):
    if splitter not in arr:
        return [arr]
    else:
        i = 0
        index = -2
        found = False
        while found == False:
            if arr[i] == splitter:
                found = True
                index = i
            i += 1
        return [arr[:index]] + splits(arr[index+length(splitter):], splitter)

# arr = "AKU DIA KAMU MEREKA"
# new_array = splits(arr, " ")
# print(new_array) #['AKU', 'DIA', 'KAMU', 'MEREKA']


def sorts(arr):
    if length(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    greater = []
    equal = []
    for element in arr:
        if element < pivot:
            less += [element]
        elif element > pivot:
            greater += [element]
        else:
            equal += [element]
    return sorts(less) + equal + sorts(greater)

# arr = [1,5,2,6,8,4,2,1]
# print(sorts(arr)) #[1, 1, 2, 2, 4, 5, 6, 8]
