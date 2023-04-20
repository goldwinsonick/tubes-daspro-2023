from typing import List
candi_list = [[1, "jin1", 2, 3, 4] for i in range(102)]+[None]

def hancurkancandi(candi_list:List) -> List:
    import recursion
    found:bool = False
    length_candi_list:int = recursion.length(candi_list)
    # Input ID candi
    inp:str = input("Masukkan ID candi: ")
    # Jika ID adalah string dan bukan number
    if (recursion.isDigit(inp) == False):
        print("Input tidak valid (Inputan harus angka!)")
        return candi_list
    inp:int = int(inp) 
    # cari candi dengan ID inp
    for i in range(length_candi_list):
        if candi_list[i][0] == inp:
            found = True
            break
    # Peringatan untuk hapus candi
    if (found == True):
        YN = input(f"Apakah anda yakin ingin menghancurkan candi ID : {inp} ? (Y/N) ")
        if (YN.upper() == "Y"):

            # Menghapus candi dengan id inp dari candi_list
            for i in range(recursion.length(candi_list)):
                if candi_list[i] != None and candi_list[i][0] == inp:
                    candi_list:List = recursion.removes(candi_list, candi_list[i],length_candi_list)

            print("Candi telah berhasil dihancurkan")
        elif (YN.upper() == "N"):
            print("Candi tidak jadi di hancurkan")
        else:
            print("Tidak valid")
    else:
        print("Tidak ada candi dengan ID tersebut.")
    return candi_list

# skema penggunaan
# candi_list = hancurkancandi(candi_list)
# print(candi_list)


def ayamberkokok(candi_list:List) -> None:
    import recursion, proses
    print("Kukuruyuk.. Kukuruyuk..")
    banyakCandi:int = recursion.length(candi_list)
    if (banyakCandi <= 99):
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noiseee*")
        print("Roro Jonggrang dikutuk menjadi candi")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    exit(1)
# skema penggunaan
# ayamberkokok(candi_list)
