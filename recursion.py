from typing import List

# Syarat pemakaian fungsi ini adalah
# 1. arr harus punya mark berupa None
# 2. Sudah tahu panjang array secara pasti dengan memasukkan length array
def length(arr: List, lengthArray: int = -1) -> int:
    panjang = 0
    if lengthArray != -1:
        return lengthArray
    elif arr == []:
        return 0
    else:
        while (arr[panjang] != None):
            panjang += 1
        return panjang

def findEmptyArrayIndex(arr: List[int], index: int = 0, lengthArray: int = -1) -> int:
    if index >= length(arr, lengthArray):
        return -99
    elif arr[index] == None:
        return index
    else:
        return findEmptyArrayIndex(arr, index + 1, lengthArray)

def isDigit(string: str, i: int = 0, lengthArray: int = -1) -> bool:
    if i == length(string, lengthArray):
        return True
    elif string[i] != '0' and string[i] != '1' and string[i] != '2' and string[i] != '3' and string[i] != '4' and string[i] != '5' and string[i] != '6' and string[i] != '7' and string[i] != '8' and string[i] != '9':
        return False
    else:
        return isDigit(string, i + 1, lengthArray)

def tail(arr: List, lengthArray: int = -1) -> None:
    new_array = [None for i in range(length(arr, lengthArray)-1)]
    if length(arr, lengthArray) == 0:
        return arr
    elif length(arr, lengthArray) == 1:
        return arr[0]
    else:
        for i in range(1, length(arr, lengthArray)):
            new_array[i-1] = arr[i]
        return new_array
    
def init(arr: List, lengthArray: int = -1) -> None:
    new_array = [None for i in range(length(arr, lengthArray)-1)]
    if length(arr, lengthArray) == 0:
        return arr
    elif length(arr, lengthArray) == 1:
        return arr[0]
    else:
        for i in range(length(arr, lengthArray)-1):
            new_array[i] = arr[i]
        return new_array

def splits(arr: str, splitter: str) -> List[str]:
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

def sorts(array, lengthArray=-1):
    panjangArray = length(array, lengthArray)
  
    def bubbleSortRecursive(n=None):
        if n is None:
            n = panjangArray
        count = 0
  
        # Base case
        if n == 1:
            return

        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
  
        if count == 0:
            return
  
        bubbleSortRecursive(n - 1)

    # Sorting array
    bubbleSortRecursive()
    return array
