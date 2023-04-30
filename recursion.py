from typing import List, Union
import time, os

# Syarat untuk penggunaan semua fungsi dengan parameter array non string
# 1. arr harus punya mark berupa None
# 2. Sudah tahu panjang array secara pasti dengan memasukkan length array
# 4. Array yang dikirimkan adalah array yang sudah melakukan proses shiftEnd atau penggeseran None di akhir
# 3. array akan diolah oleh fungsi dan direturn bersama dengan marknya

#  ** REKURSIF 1
# Fungsi length mengembalikan panjang array yang dihitung tanpa mark
def length(arr: List, lengthArray: int = -1, i: int = 0) -> int:
    # jika panjang array sudah diketahui eksplisit
    if lengthArray != -1:
        return lengthArray
    # Basis
    elif arr == []:
        return 0
    elif arr[i] == None:
        return i
    # Rekurens
    else:
        return length(arr, lengthArray, i+1)

#  ** REKURSIF 2
# Fungsi findEmptyArrayIndex mendeteksi dan mengembalikan index array dengan mark None pertama kali
# atau index yang masih belum memiliki nilai alias kosong
def findEmptyArrayIndex(arr: List, index: int = 0, lengthArray: int = -1) -> int:
    arr_len: int = length(arr, lengthArray)
    # Basis
    if index > arr_len:
        return -99
       # Mengecek apakah index ada nilai kosong sebelum mark
    elif arr[index] == None and (arr[-2] == None and arr[-1] == None):
        return index
    # Rekurens
    else:
        return findEmptyArrayIndex(arr, index + 1, arr_len)

# ** REKURSIF 3
# Fungsi isDigit digunakan untuk mengatasi error jika user memasukkan selain angka, diakibatkan block try except
# Fungsi isDigit akan mengembalikan boolean True jika semua komponen dari array atau string adalah digit angka
def isDigit(string: str, i: int = 0) -> bool:
    # Basis { kalau sampai ujung string gak ada yang membuatnya False }
    if i == len(string):
        return True
    elif string[i] != '0' and string[i] != '1' and string[i] != '2' and string[i] != '3' and string[i] != '4' and string[i] != '5' and string[i] != '6' and string[i] != '7' and string[i] != '8' and string[i] != '9':
        return False
    # Rekurens
    else:
        return isDigit(string, i + 1)

#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# Fungsi tail_string mengembalikan array bentuk string tanpa nilai dari bagian depan hingga index atau
# hanya mengembalikan array yang dengan index lebih besar dari parameter index
def tail_string(string: str, index: int) -> str:
    new_string: Union[List, str] = [None for i in range((len(string))-index)]
    if len(string) <= 1:
        return string
    else:
        for i in range(index, len(string)):
            new_string[i-index] = string[i]
        return "".join(new_string)


#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# Fungsi init_string mengembalikan array bentuk string tanpa nilai dari bagian index hingga bagian belakang atau
# hanya mengembalikan array yang dengan index lebih kecil dar index yang dikirimkan melalui params
def init_string(string: str, index: int) -> str:
    new_string: Union[List, str] = [None for i in range(index)]
    if len(string) <= 1:
        return string
    else:
        for i in range(index):
            new_string[i] = string[i]
        return "".join(new_string)

#! Khusus untuk array yang berupa string karena diizinkan penggunaan len untuk string
# ** REKURSIF 4
# Fungsi split mengembalikan array yang berisi string hasil pemisahan dari splitter params
def splits(arr: str, splitter: str, add_none: bool = False) -> List[str]:
    # Rekurens
    for i in range(len(arr)):
        if arr[i] == splitter:
            return [init_string(arr, i)] + splits(tail_string(arr, i+len(splitter)), splitter, add_none)
    # Basis
    if add_none: # menambahkan marks diakhir
        return [arr, None]
    else:
        return [arr]

# ** REKURSIF 5
# Fungsi sorts mengembalikan array yang telah diurutkan dengan mark None menggunakan bublesort principle
def sorts(array: List, lengthArray: int = -1) -> List:
    panjangArray: int = length(array, lengthArray)
    # Untuk kebutuhan rekursif
    def bubbleSortRecursive(n:int = None) -> None :
        if n == None:
            n = panjangArray
        count = 0
        # Basis
        if n == 1:
            return None
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
        # Rekurens
        if count == 0:
            return bubbleSortRecursive(n - 1)
    # Sorting array
    bubbleSortRecursive()
    return array
# Contoh penggunaan
# array = [1.1212,4.121,2,5,8, None]
# print(sorts(array))

# ** REKURSIF 6
# Fungsi strips menghilangkan string pindah baris dari hasil pembacaan csv
def strips(text: str, i: int = 0, new_text: str = '') -> str:
    # Basis
    if i == len(text):
        return new_text
    # Rekurens
    else:
        if text[i] != '\n':
            new_text += text[i]
        return strips(text, i + 1, new_text)

# Fungsi shiftToEnd ini akan mengembalikan array dengan memindahkan array index tertentu ke bagian akhir atau index -1
def shiftToEnd(arr: List, index: int, arrayLength: int) -> List:
    arr_len: int = length(arr, arrayLength)
    # Jika index di luar range array atau sudah di ujung kanan, langsung return pesan kesalahan
    if index < 0 or index >= arr_len:
        return print("Out index of array")
    # Jika index valid, lakukan shift ke kanan
    temp: Union[str, None, int, float] = arr[index]
    for i in range(index, arr_len - 1):
        arr[i] = arr[i+1]
    arr[arr_len - 1] = temp
    return arr

# Fungsi read_csv mengkonversi csv menjadi array baru dengan mark
def read_csv(filename: str, delimiter: str = ';') -> List:
    with open(filename) as file:
        parse: List = [None]
        line_num: int = 0
        # Membaca semua line dengan iterasi
        for line in file:
            if line_num == 0:
                line_num += 1
                continue
            values: List = splits(strips(line), delimiter)
            parse: List = appends(parse, values)
    return parse

# Fungsi write_csv mengkonversi dari array menjadi file csv 
def write_csv(filename: str, to_write: Union[str, None], len_col: int) -> None:
    with open(filename, "w") as file:
        rows: int = length(to_write)
        if rows != 0:
            cols = len_col  # karena jumlah column sama tiap garis
            for i in range(rows):
                if to_write[i] != None:
                    for j in range(cols):
                        file.write(str(to_write[i][j]))
                        if j < cols-1:
                            file.write(";")
                    if i < rows-1:
                        file.write("\n")
        else:
            print("Matriks kosong! Tidak bisa menuliskan file.")

# Fungsi appends mengembalikan array dengan tambahan new_values di akhir dengan mark
def appends(arr: list, new_values: List, start_position: bool = False) -> List:
    temp_new_arr: List = [None for i in range(length(arr)+2)]
    if start_position == False:
        # copy data dari array sebelumnya
        for i in range(length(arr)):
            temp_new_arr[i] = arr[i]
        # Copy data baru dengan mark baru ke array sebelumnya
        empty_index_array_temp_arr = findEmptyArrayIndex(temp_new_arr)
        temp_new_arr[empty_index_array_temp_arr] = new_values
        # Kembalikan ke array dengan data yang sudah update
        arr = temp_new_arr
    # Menambahkan data pada index awal array
    else:
        for i in range(1, length(arr)+1):
            temp_new_arr[i] = arr[i-1]
        # Copy data baru dengan mark baru ke candi_list sebelumnya
        temp_new_arr[0] = new_values
        # Kembalikan ke candi_list dengan data yang sudah update
        arr: List = temp_new_arr
    return arr

# Fungsi removes mengembalikan array baru yang telah dihapus deletedValue yang merupakan komponen dari array tersebut
def removes(arr: List, deletedValue: List, lengthInitial: int) -> List:
    # wadah hasil akhir array yang telah dihapus
    arr_clear: List = [None for i in range(lengthInitial)]
    # cari index deletedValue dalam array yang pertama kali muncul
    index: int = -99
    for i in range(lengthInitial):
        if arr != None and arr[i] == deletedValue:
            index = i
            break
    # Copy semua data dari arr kecuali nilai deletedValue ke wadah
    for k in range(lengthInitial):
        if k != index:
            arr_clear[k] = arr[k]
    arr: List = shiftToEnd(arr_clear, index, lengthInitial)
    return arr

# Fungsi outputtipejin menghandle output untuk role tipe jin
def outputtipejin(tipe: str) -> str:
    output: str = ""
    if tipe == "jin_pembangun":
        output = "Pembangun"
    else:
        output = "Pengumpul"
    return output

# Fungsi clear untuk membersihkan terminal  
def clear() -> None:
    os.system('cls')

# Fungsi delay untuk memberikan ejek jeda pada eksekusi program
def delay(seconds: int) -> None:
    time.sleep(seconds)
