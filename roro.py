from typing import List, Union
candi_list = [[1, "jin1", 2, 3, 4], [2, "jin1", 2, 3, 4], None]


def hancurkancandi(candi_list:List):
    import recursion
    inp:str = input("Masukkan ID candi: ")
    found:bool = False
    length_candi_list:int = recursion.length(candi_list)
    if (recursion.isDigit(inp) == False):
        print("Input tidak valid (Inputan harus angka!)")
        return
    inp:int = int(inp)
    print(inp)
    for i in range(length_candi_list):
        if candi_list[i][0] == inp:
            found = True
            break
    if (found == True):
        YN = input(
            "Apakah anda yakin ingin menghancurkan candi ID : "+str(inp) + "? (Y/N)")
        if (YN.upper() == "Y"):

            # Menghapus candi dengan id tersebut dari candi_list
            for i in range(recursion.length(candi_list)):
                if candi_list[i] != None and candi_list[i][0] == inp:
                    #    copy data dari deleted candi sebelumnya
                    # copy data dengan mengurangi 1 index dengan tanpa menyertakan candi_list[i]
                    candi_clear = [None for i in range(length_candi_list)]
                    for k in range(length_candi_list):
                        if candi_list[k] != candi_list[i]:
                            candi_clear[k] = candi_list[k]

                    candi_list = candi_clear
                    recursion.shiftToEnd(candi_list, i, length_candi_list)

            print("Candi telah berhasil dihancurkan")
        elif (YN.upper() == "N"):
            print("Candi tidak jadi di hancurkan")
        else:
            print("Tidak valid")
    else:
        print("Tidak ada candi dengan ID tersebut.")
    return candi_list


# candi_list = hancurkancandi(candi_list)
# print(candi_list)


def ayamberkokok(candi_list:List)->None:
    import recursion
    print("Kukuruyuk.. Kukuruyuk..")
    banyakCandi:int = recursion.length(candi_list)
    if (banyakCandi <= 99):
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noiseee*")
        print("Roro Jonggrang dikutuk menjadi candi")
    elif (banyakCandi >= 100):
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Roro Jonggrang menangggg!")
    # Exit program (Harus ada fungsi exit() di proses.py dulu)
