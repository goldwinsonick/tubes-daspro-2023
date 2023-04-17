from typing import List

# Syarat untuk penggunaan semua fungsi dengan parameter array non string
# 1. arr harus punya mark berupa None
# 2. Sudah tahu panjang array secara pasti dengan memasukkan length array
# 4. Array yang dikirimkan adalah array yang sudah melakukan proses shiftEnd atau penggeseran None di akhir
# 3. array akan diolah oleh fungsi dan direturn bersama dengan marknya

# Fungsi length mengembalikan panjang array tanpa mark
# Params kedua tidaklah wajib, params lengthArray jika panjang array sudah diketahui secara eksplisit
def length(arr: List, lengthArray: int = -1) -> int:
    panjang:int = 0
    if lengthArray != -1:
        return lengthArray
    elif arr == []:
        return 0
    else:
        while (arr[panjang] != None):
            panjang += 1
        return panjang
# # contoh penggunaan
# arr = [1,2,4,5,6,2, None]
# print(length(arr))s


#  ** REKURSIF 1
# Fungsi findEmptyArrayIndex mendeteksi dan mengembalikan index array dengan mark None pertama kali
# atau index yang masih belum memmiliki nilai alias kosong
# Params kedua dan ketiga tidaklah wajib
# Params index untuk kebutuhan rekursi
# Params lengthArray jika panjang array sudah diketahui secara eksplisit
def findEmptyArrayIndex(arr: List, index: int = 0, lengthArray: int = -1) -> int:
    arr_len:int = length(arr, lengthArray)
    if index > arr_len:
        return -99
    elif arr[index] == None and (arr[-2] == None and arr[-1] == None):
        return index
    else:
        return findEmptyArrayIndex(arr, index + 1, arr_len)
# contoh penggunaan
# arr1 = [0, 2, 3, 4, None, None]
# print(findEmptyArrayIndex(arr1))  # output: 5
# arr2 = [0, 2, 3, 4, None]
# print(findEmptyArrayIndex(arr2))  # output: -99


# ** REKURSIF 2
# Fungsi isDigit digunakan untuk mengatasi error jika user memasukkan selain angka, diakibatkan block try except
# Fungsi isDigit akan mengembalikan boolean True jika semua komponen dari array atau string adalah digit angka
# Params kedua tidak wajib, params i untuk kebutuhan rekursi
def isDigit(string: str, i: int = 0) -> bool:
    if i == len(string):
        return True
    elif string[i] != '0' and string[i] != '1' and string[i] != '2' and string[i] != '3' and string[i] != '4' and string[i] != '5' and string[i] != '6' and string[i] != '7' and string[i] != '8' and string[i] != '9':
        return False
    else:
        return isDigit(string, i + 1)
# contoh penggunaan :
# arr = "192038019s"
# arr1 = "192038019"
# print(isDigit(arr))
# print(isDigit(arr1))


# Fungsi tail mengembalikan array tanpa nilai dari bagian depan hingga index atau
# hanya mengembalikan array yang dengan index lebih besar dari parameter index
# Params kedua tidaklah wajib,
# Params lengthArray jika panjang array sudah diketahui secara eksplisit
def tail(arr: List, lengthArray: int = -1) -> None:
    from typing import List
    new_array:List = [None for i in range(length(arr, lengthArray))]
    if length(arr, lengthArray) == 0:
        return arr
    elif length(arr, lengthArray) == 1:
        return arr[0]
    else:
        for i in range(1, length(arr, lengthArray)):
            new_array[i-1] = arr[i]
        return new_array
# contoh penggunaan
# arr = [2,1,2,12,1,3,None]
# print(tail(arr))


# Fungsi init mengembalikan array tanpa nilai dari bagian index hingga bagian belakang atau
# hanya mengembalikan array yang dengan index lebih kecil dar index yang dikirimkan melalui params
# Params kedua tidaklah wajib,
# Params lengthArray jika panjang array sudah diketahui secara eksplisit
def init(arr: List, lengthArray: int = -1) -> None:
    from typing import List
    new_array:List = [None for i in range(length(arr, lengthArray))]
    if length(arr, lengthArray) == 0:
        return arr
    elif length(arr, lengthArray) == 1:
        return arr[0]
    else:
        for i in range(length(arr, lengthArray)-1):
            new_array[i] = arr[i]
        return new_array
# contoh penggunaan
# arr = [2,1,2,12,1,3,None]
# print(init(arr))


#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# Fungsi tail_string mengembalikan array bentuk string tanpa nilai dari bagian depan hingga index atau
# hanya mengembalikan array yang dengan index lebih besar dari parameter index
def tail_string(string: str, index: int) -> str:
    from typing import List, Union
    new_string:Union[List, str]= [None for i in range((len(string))-index)]
    if len(string) <= 1:
        return string
    else:
        for i in range(index, len(string)):
            new_string[i-index] = string[i]
        return "".join(new_string)
# # contoh penggunaan 
# string = "Aku Suka Kamu"
# print(tail_string(string,3))

#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# Fungsi init_string mengembalikan array bentuk string tanpa nilai dari bagian index hingga bagian belakang atau
# hanya mengembalikan array yang dengan index lebih kecil dar index yang dikirimkan melalui params
def init_string(string: str, index: int) -> str:
    from typing import List, Union
    new_string:Union[List, str] = [None for i in range(index)]
    if len(string) <= 1:
        return string
    else:
        for i in range(index):
            new_string[i] = string[i]
        return "".join(new_string)
# # contoh penggunaan 
# string = "Aku Suka Kamu"
# print(init_string(string,3))

#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# ** REKURSIF 3
# Fungsi split mengembalikan array yang berisi string hasil pemisahan dari splitter params
def splits(arr: str, splitter: str) -> List[str]:
    for i in range(len(arr)):
        if arr[i] == splitter:
            return [init_string(arr, i)] + splits(tail_string(arr, i+len(splitter)), splitter)
    return [arr]
# contoh penggunaan
# arr = "I LOVE U <3"
# print(splits(arr, " "))


# ** REKURSIF 4
# Fungsi sorts mengembalikan array yang telah diurutkan dengan mark None menggunakan bublesort principle
# Syarat array harus mempunyai mark berupa None
def sorts(array: List, lengthArray: int = -1) -> List:
    panjangArray:int = length(array, lengthArray)

    def bubbleSortRecursive(n=None):
        if n == None:
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
# Contoh penggunaan
# array = [1.1212,4.121,2,5,8, None]
# print(sorts(array))


# Fungsi ini ketika digunakan wajib menyertakan semua parameter
# fungsi ini akan mengembalikan array dengan memindahkan array index tertentu ke bagian akhir atau index -1
def shiftToEnd(arr: List, index: int, arrayLength: int) -> List:
    from typing import Union
    arr_len:int = length(arr, arrayLength)
    # Jika index di luar range array atau sudah di ujung kanan, langsung return pesan kesalahan
    if index < 0 or index >= arr_len:
        return print("Out index of array")
    # Jika index valid, lakukan shift ke kanan
    temp:Union[str,None,int,float] = arr[index]
    for i in range(index, arr_len - 1):
        arr[i] = arr[i+1]
    arr[arr_len - 1] = temp
    return arr
# contoh penggunaan
# arr = [1, 2, 3, 4, None, 6, 7]
# print(shiftToEnd(arr, 4, 7))

def read_csv(filename, delimiter=';'):
    with open(filename) as file:
        parse = []
        for line in file:
            values = splits(line, delimiter)
            parse += [values]
    return parse


def write_csv(filename, to_write):
    with open(filename, "w") as file:
        rows = length(to_write)
        if rows != 0:
            cols = length(to_write[0])  # karena jumlah column sama tiap garis
            for i in range(rows):
                for j in range(cols):
                    file.write(str(to_write[i][j]))
                    if j < cols-1:
                        file.write(";")
                if i < rows-1:
                    file.write("\n")
        else:
            print("Matriks kosong! Tidak bisa menuliskan file.")
